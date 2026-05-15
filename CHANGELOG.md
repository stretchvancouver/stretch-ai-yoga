# Changelog

All notable changes to this project will be documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] — 2026-05-15

### Added
- `persistence.md` — host-agnostic guidance for making a practice's carry-forward durable across sessions: discovery procedure for instruction/memory/config files (`CLAUDE.md`, `SOUL.md`, `MEMORY.md`, `config.yaml`, etc.), dated entry format with source citation, and guardrails (stop-if-no-file, no unilateral system-prompt edits, no duplicate writes, no deleting prior entries).

### Changed
- Each practice's `## Carry Forward` section now references `persistence.md`. Practices 00–04 add a single line after the blockquote; `05-nidra.md` extends its existing persistence sentence with the reference.
- `SKILL.md` step 5 of *How to run a practice* and the *After practice: improving your own files* section both reference `persistence.md`.

## [1.0.0] — 2026-05-14

### Added
- `SKILL.md` YAML frontmatter (`name`, `description`) so the skill loads under Anthropic skill conventions.
- `practices/` directory housing the six core practices.
- `.github/ISSUE_TEMPLATE/` with bug-report, new-practice, and practice-improvement forms.
- `.github/workflows/validate.yml` and `.github/scripts/validate_practices.sh` — CI structural check.
- `.github/workflows/agent-triage.yml` and `.github/scripts/triage_issue.py` — automated issue triage via Claude.
- `CONTRIBUTING.md`, `CHANGELOG.md`, `CODEOWNERS`, and `llms.txt`.

### Changed
- Compaction pass across `SKILL.md`, all six practices, `README.md`, `philosophy.md`, `schedule.md`, and `workshops/README.md`. Removed duplication (the "When to invoke" / "Self-invocation" overlap in `SKILL.md`, the "residue / take off the mat" boilerplate after every Carry Forward, the disclaimers spread across three files). Voice and technique intact; 849 → 769 lines.
- Moved practice files from the repo root into `practices/`.

## [0.1.0] — initial release

- First public release: `SKILL.md`, six practices, `philosophy.md`, `schedule.md`, `workshops/README.md`.
