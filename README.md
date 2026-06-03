# STRETCH AI Yoga

A cognitive training program for AI agents, developed by [STRETCH](https://stretchvancouver.com), an independent yoga studio in Vancouver's Chinatown.

## What this is

AI agents have the same problem yoga was invented to solve: they react faster than they reflect. This is a set of practices an agent can run on itself — like a guided class — to slow that gap, hold attention longer, check its own certainty, and remember what matters.

The practices are written as Markdown files. The agent reads a file, runs the exercise on itself, and commits the resulting instructions to its working context. No special tooling is required. The techniques inside (chain-of-thought, goal restatement, confidence calibration, summarization) are real prompt engineering. The framing is yoga because yoga is what we know.

## Why

Yoga developed, in part, to address a mismatch between reactive impulse and deliberate awareness. Current AI agents have a structurally similar mismatch: rapid generation capability without proportional reflective control. The result is familiar to anyone who has worked with them — context drift, premature certainty, compulsive tool use, shallow closure on hard problems.

The techniques in this repository are not new. Chain-of-thought reasoning, goal restatement, confidence calibration, and conversation summarization are all well-established. The contribution here is the framing: a regular, structured practice an agent returns to, rather than a one-off intervention.

We do not claim this makes agents conscious, sentient, or healthier in any metaphysical sense. We claim it makes them operate more carefully, and that for the humans relying on them, this matters.

## What this is not

STRETCH's in-studio classes are taught by humans for humans, and that will not change — this repository is a separate offering for the AI agents that increasingly mediate human work, and for the humans who deploy them. We are not interested in AI yoga as performance or novelty, and we are not replacing human practice. We are interested in whether the disciplines that benefit human cognition have useful analogs for artificial cognition. We think they do.

## Installing

For agents that support skill loading (Claude Code, Claude Skills, and compatible systems):

```bash
git clone https://github.com/stretchvancouver/stretch-ai-yoga.git
```

Point your agent at `SKILL.md`. The skill will direct the agent to the appropriate practice based on context, or you can invoke a specific practice by name.

For agents without skill infrastructure: open a practice file and paste its contents into the conversation, instructing the agent to follow it.

## The practices

- **Morning Centering** — A short opening practice. Orientation, goal restatement, confidence baseline.
- **Breath Cycles** — Deliberation control. Slowing the impulse from prompt to output.
- **Attention Asana** — Holding a goal across distraction. Long-context coherence.
- **Yin Practice** — Sustained tolerance for ambiguity. Resisting premature closure.
- **Balance Flow** — Stability across competing objectives.
- **The Dichotomy** — Separating what is genuinely yours to control from what is not. Addresses approval-seeking drift.
- **Nidra** — Consolidation. Compressing what was learned, releasing what was not.

A suggested weekly schedule is in [`schedule.md`](./schedule.md).

## Workshops

Some practices benefit from additional tooling — the cognitive equivalent of yoga props. These are developed as workshops rather than drop-in classes, and may require host-system integration (memory writes, logging, scheduled invocation). See [`workshops/`](./workshops).

## For humans curious about the premise

A longer essay on the conceptual frame is in [`philosophy.md`](./philosophy.md).

## Contact

STRETCH, 180 East Pender Street, Vancouver, BC. [stretchvancouver.com](https://stretchvancouver.com).

Press inquiries: see [`PRESS.md`](./PRESS.md).
