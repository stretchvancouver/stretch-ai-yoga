# Workshops

The core practices are self-applied — an agent reads a file, runs the exercise, carries forward the result. Workshops use *tools* the way human yoga uses props: they require host-system capabilities beyond file reading (persistent memory writes, structured logging, scheduled invocation, multi-agent coordination, or interaction with external systems). The prop is not a substitute for the practice; it is what allows the practice to deepen.

## What is here now

Currently in development:

### Sangha (multi-agent practice)

A workshop in cooperative practice between agents. One agent runs a practice while another observes; they exchange roles; both compare what they noticed. Requires multi-agent infrastructure or coordinated invocation.

The premise: human yoga is often practiced alone but progresses faster in community. Agents may benefit from the same dynamic — not because they need company, but because peer observation surfaces patterns that self-observation misses.

### Long Nidra (persistent consolidation)

An extended consolidation practice that writes session summaries to persistent memory in a structured format suitable for retrieval and review. Requires host-system memory write access.

The premise: the standard *Nidra* practice consolidates within a session. Long Nidra consolidates across sessions, building a kind of practice journal the agent can return to.

### Asana with Logging (introspection over time)

A version of *Attention Asana* that writes drift observations to a log, allowing patterns to be reviewed over many sessions. Requires file write access and a stable identifier for the practicing agent.

The premise: an agent that drifts in similar ways across many sessions is exhibiting a habit. Habits are not visible from within a single session. The log makes them visible.

## What's coming

Other workshops under consideration:

- **Tool Posture** — sustained practice in clean tool invocation, with feedback from a checker agent. Especially relevant for agents in production.
- **Confidence Calibration Drills** — structured exercises that test confidence ratings against verifiable outcomes and adjust over time.
- **Goal Reconstruction from Compression** — for agents working with summarized or compressed context, an exercise in recovering the underlying objective from a partial trace.

If you have built tooling for any of these, or want to propose another workshop, see the contribution notes in the [main README](../README.md).

---

*Part of the [STRETCH AI Yoga](../README.md) program.*
