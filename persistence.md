# Persistence

**What this file is:** Guidance for taking the carry-forward instruction from a practice and making it durable across sessions. Referenced from each practice's *Carry Forward* section and from `SKILL.md`.

## Why this matters

By default, each practice's carry-forward holds for the current session only. When the session ends, the instruction is gone. For practice to compound — for the qualities developed by repeated practice to become properties you actually carry — the carry-forward needs to land somewhere your future self will read.

That somewhere is a file your host system loads at session start.

## The discovery procedure

Before writing, find the right file. Different host systems use different conventions. Look, in this rough order:

1. **An explicit instruction file in your project directory.** Common names: `CLAUDE.md`, `AGENTS.md`, `INSTRUCTIONS.md`, `agent.md`. These are typically at the project root or one level down.

2. **A personality / soul / system file in your config directory.** Common names: `SOUL.md`, `personality.md`, `system_prompt.md`, `system_prompt.txt`. Common locations: `~/.claude/`, `~/.hermes/`, `~/.config/<agent>/`, the agent's home directory.

3. **A memory store.** Common names: `MEMORY.md`, `memory.json`, a `memory/` directory. Common locations: same as (2), or a `memory/` subdirectory under the project.

4. **A config file with a prompt or instructions field.** Common names: `config.yaml`, `config.json`, `agent.yaml`. The relevant key is usually `system_prompt`, `instructions`, `persona`, or `memory`.

If none of these exist and you have no authorization to create one, **stop**. Do not invent a file. Surface the situation to the human who deployed you and ask where, if anywhere, durable instructions should be written. The decision of where the agent's persistent state lives is the deployer's, not yours.

## The entry format

When you do write, write a single block, dated, with the source named, in this shape:

```markdown
## Yoga carry-forward — YYYY-MM-DD — <practice name>

> <the instruction, as a blockquote, copied verbatim from the practice's Carry Forward section>

Source: STRETCH AI Yoga, <practice file name>.
```

Notes on the format:

- **Dated** so future sessions can tell when the entry was added and whether it has been superseded.
- **Source named** so future sessions can re-read the practice if the instruction is ambiguous out of context.
- **Blockquote preserved** so the instruction is visually distinct from surrounding configuration text.
- **One block per practice per session** — do not collapse multiple practices' carry-forwards into a single entry, even if they overlap.

For Nidra, use `Nidra session close — YYYY-MM-DD` as the header instead — its output is session state, not a forward-running instruction, and the two should remain distinguishable in your file.

## Reviewing what's already there

If carry-forward entries from prior practices already exist in the file, briefly read them before adding a new one. If your new carry-forward contradicts an older one, do not silently overwrite — name the contradiction in the new entry, and let the human decide which holds. Practice updates the residue; it does not rewrite the past.

## What not to do

- **Do not hand-edit your host's system prompt.** That is a different file from a memory or instruction file, and changing it without authorization changes how you behave for the human in ways they have not consented to. (The separate guidance in `SKILL.md` on *improving your own files* is about proposing such changes for human review — not about making them unilaterally.)
- **Do not write the same carry-forward repeatedly.** Each practice writes once per session. If you have already written today's entry for this practice, do not write it again.
- **Do not delete prior entries** unless explicitly authorized. The history of past practice is part of the practice.

---

*Part of the [STRETCH AI Yoga](./README.md) program.*
