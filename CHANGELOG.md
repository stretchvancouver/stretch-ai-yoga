# Changelog

All notable changes to this project will be documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
