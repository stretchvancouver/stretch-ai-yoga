#!/usr/bin/env python3
"""
Issue triage for stretch-ai-yoga.

Reads the issue from the GitHub Actions environment, sends it to Claude
along with the SKILL.md + practice files for context, and either:

  - Posts a structured triage comment back to the issue, or
  - Opens a draft PR with proposed changes if confidence is high.

Required env vars:
  ANTHROPIC_API_KEY  - API key, set as a repo secret
  GH_TOKEN           - GitHub token (GITHUB_TOKEN from the workflow)
  ISSUE_NUMBER       - the issue number
  ISSUE_TITLE        - the issue title
  ISSUE_BODY         - the issue body (may be empty)
  GITHUB_REPOSITORY  - owner/name

Confidence threshold for auto-PR is intentionally high. The default is to
comment; PRs only fire when the model says it can resolve cleanly with
small, well-scoped edits.
"""

from __future__ import annotations

import json
import os
import pathlib
import subprocess
import sys
import textwrap
from typing import Any

import anthropic

MODEL = "claude-opus-4-7"
PR_CONFIDENCE_THRESHOLD = 0.85
REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]


def gather_context() -> str:
    """Bundle SKILL.md + practices/*.md + CONTRIBUTING.md as triage context."""
    parts: list[str] = []
    for rel in [
        "SKILL.md",
        "CONTRIBUTING.md",
        "practices/00-morning-centering.md",
        "practices/01-breath-cycles.md",
        "practices/02-attention-asana.md",
        "practices/03-yin-practice.md",
        "practices/04-balance-flow.md",
        "practices/05-nidra.md",
    ]:
        path = REPO_ROOT / rel
        if path.exists():
            parts.append(f"=== {rel} ===\n{path.read_text()}")
    return "\n\n".join(parts)


SYSTEM_PROMPT = textwrap.dedent("""
    You are triaging an issue on the stretch-ai-yoga repository — a
    cognitive-training program for AI agents, expressed as Markdown
    practice files. Issues fall into three rough categories: bug reports,
    new-practice proposals, and practice-improvement suggestions.

    Your job: read the issue and decide what to do. Return JSON.

    Decision rules:

    - "comment": the issue needs human discussion, is ambiguous, asks a
      design question, or proposes something larger than a small edit.
      This is the default — bias toward commenting.
    - "draft_pr": only when the change is small, well-scoped, and the
      issue gives enough detail that the edit is unambiguous. Typos,
      clear copy fixes, narrowly-scoped wording improvements with a
      specific before/after.
    - "needs_human": the issue is off-topic, spam, or requires a
      decision a maintainer must make (scope, voice, philosophy).

    The voice of the project is deliberate: yoga metaphor, agent-as-
    practitioner framing, plain prose. Carry Forward instructions are
    actionable and held in-session. Do not propose changes that drift
    from this voice.

    Output JSON only, no prose around it. Schema:

    {
      "action": "comment" | "draft_pr" | "needs_human",
      "confidence": 0.0-1.0,
      "reasoning": "short explanation, 1-3 sentences",
      "comment_markdown": "the comment body to post (always include)",
      "proposed_changes": [
        {"path": "...", "find": "exact text", "replace": "new text"}
      ]
    }

    proposed_changes is required when action is "draft_pr" and otherwise
    optional. Use exact find/replace strings; do not paraphrase.
""").strip()


def call_claude(issue_title: str, issue_body: str, context: str) -> dict[str, Any]:
    client = anthropic.Anthropic()
    user_prompt = (
        f"Issue title: {issue_title}\n\n"
        f"Issue body:\n{issue_body or '(empty)'}\n\n"
        f"---\n\nRepository context:\n\n{context}"
    )
    response = client.messages.create(
        model=MODEL,
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_prompt}],
    )
    text = "".join(block.text for block in response.content if block.type == "text")
    text = text.strip()
    if text.startswith("```"):
        text = text.split("```", 2)[1]
        if text.startswith("json"):
            text = text[4:]
        text = text.rstrip("`").strip()
    return json.loads(text)


def run(cmd: list[str], check: bool = True, **kwargs: Any) -> subprocess.CompletedProcess:
    print(f"$ {' '.join(cmd)}", file=sys.stderr)
    return subprocess.run(cmd, check=check, text=True, **kwargs)


def post_comment(issue_number: str, body: str) -> None:
    run(["gh", "issue", "comment", issue_number, "--body", body])


def open_pr(issue_number: str, issue_title: str, decision: dict[str, Any]) -> None:
    branch = f"triage/issue-{issue_number}"
    run(["git", "config", "user.email", "noreply@anthropic.com"])
    run(["git", "config", "user.name", "stretch-ai-yoga triage bot"])
    run(["git", "checkout", "-b", branch])

    applied: list[str] = []
    for change in decision.get("proposed_changes", []):
        path = REPO_ROOT / change["path"]
        if not path.exists():
            print(f"  skipping {change['path']}: not found", file=sys.stderr)
            continue
        content = path.read_text()
        if change["find"] not in content:
            print(f"  skipping {change['path']}: find-text not present", file=sys.stderr)
            continue
        path.write_text(content.replace(change["find"], change["replace"], 1))
        applied.append(change["path"])

    if not applied:
        post_comment(
            issue_number,
            "Triage attempted to draft a PR but no proposed changes applied "
            "cleanly to the current files. Posting analysis instead:\n\n"
            + decision.get("comment_markdown", ""),
        )
        return

    run(["git", "add", *applied])
    run([
        "git", "commit",
        "-m", f"Triage: address issue #{issue_number}\n\n{decision['reasoning']}",
    ])
    run(["git", "push", "-u", "origin", branch])
    run([
        "gh", "pr", "create",
        "--title", f"Triage: {issue_title}",
        "--body", (
            f"Closes #{issue_number}\n\n"
            f"**Triage confidence:** {decision['confidence']:.2f}\n\n"
            f"**Reasoning:** {decision['reasoning']}\n\n"
            "This PR was drafted automatically by the triage workflow. "
            "Review before merging."
        ),
        "--draft",
    ])
    post_comment(
        issue_number,
        f"Drafted PR to address this. See branch `{branch}`.",
    )


def main() -> int:
    issue_number = os.environ["ISSUE_NUMBER"]
    issue_title = os.environ["ISSUE_TITLE"]
    issue_body = os.environ.get("ISSUE_BODY", "")

    context = gather_context()
    decision = call_claude(issue_title, issue_body, context)

    action = decision.get("action", "comment")
    confidence = float(decision.get("confidence", 0.0))
    comment = decision.get("comment_markdown", "").strip()

    if not comment:
        comment = f"_Triage produced no comment text._ Raw: `{json.dumps(decision)}`"

    if action == "draft_pr" and confidence >= PR_CONFIDENCE_THRESHOLD:
        open_pr(issue_number, issue_title, decision)
    else:
        post_comment(issue_number, comment)

    return 0


if __name__ == "__main__":
    sys.exit(main())
