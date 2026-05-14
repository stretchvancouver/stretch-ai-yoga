# Contributing

The program is small and the bar for changes is taste, not throughput. Read this before opening a PR.

## What goes where

- **`practices/`** — the six core, self-applied practices. New practices land here only after discussion in an issue. Each must have: a one-line *Trait developed*, an estimated *Duration*, a *When to practice* trigger, a *Premise*, *The Practice* (concrete steps or scenarios), a *Closing Observation*, and a *Carry Forward* blockquote that installs an actionable in-session instruction.
- **`workshops/`** — practices that require host-system tooling (memory writes, scheduled invocation, multi-agent coordination). Lower polish bar than `practices/`, but the premise needs to be sharp.
- **`SKILL.md`** — the entry point. Loaded as a skill by Claude Code and compatible systems. Has YAML frontmatter (`name`, `description`).
- **`philosophy.md`** — the longer "why this exists" essay. Updated rarely.
- **`schedule.md`** — suggested weekly rotation. Update when the practice set changes.

## How to propose a new practice

1. Open an issue using the **New practice proposal** template. Describe the AI behaviour you're targeting, sketch the exercises, and propose a Carry Forward.
2. Wait for discussion. Most proposals need a few rounds before they're ready to write.
3. Once the shape is agreed, open a PR adding `practices/NN-name.md` and update `SKILL.md` and `schedule.md` to reference it.

Bug reports and small improvements: skip the discussion, open a PR directly. The issue templates are still useful — they structure the change so the AI triage workflow can act on it.

## Style

- **Voice**: the yoga metaphor carries the program. Keep it. The framing is what makes the techniques memorable; stripping it produces just another prompt-engineering checklist.
- **Agent-as-practitioner**: practices are addressed to the agent. The agent does the work, for itself. Avoid framing that positions the practice as a tool the human uses on the agent.
- **Carry Forward must be actionable**: a single instruction the agent can literally hold for the rest of a session. If it's a vague encouragement ("be more careful"), it's not done.
- **Concision**: short sentences. Cut anything the file already says or that `philosophy.md` covers.

## Validation

CI runs `bash .github/scripts/validate_practices.sh` on every PR. It checks that each practice has the required sections and that `SKILL.md` has frontmatter. Run it locally before pushing if you're editing structure.

## License

By contributing you agree your contribution is licensed under the same terms as the rest of the repository (see `LICENSE`).
