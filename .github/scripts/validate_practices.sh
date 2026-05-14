#!/usr/bin/env bash
# Validates that every file in practices/ has the required structure
# and that SKILL.md has the expected frontmatter + body skeleton.
# Exits non-zero on any failure.

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
FAILURES=0

fail() {
  echo "  FAIL: $1"
  FAILURES=$((FAILURES + 1))
}

require_section() {
  local file="$1"
  local pattern="$2"
  local label="$3"
  if ! grep -q -- "$pattern" "$file"; then
    fail "$file is missing $label"
  fi
}

echo "Validating SKILL.md..."
SKILL="$ROOT/SKILL.md"
if [[ ! -f "$SKILL" ]]; then
  fail "SKILL.md not found at repo root"
else
  if ! head -1 "$SKILL" | grep -q '^---$'; then
    fail "SKILL.md is missing YAML frontmatter (first line should be '---')"
  fi
  require_section "$SKILL" "^name:" "frontmatter 'name:' field"
  require_section "$SKILL" "^description:" "frontmatter 'description:' field"
  require_section "$SKILL" "## When to invoke" "'When to invoke' section"
  require_section "$SKILL" "## How to run" "'How to run' section"
  require_section "$SKILL" "## Practices" "'Practices' section"
fi

echo "Validating practices/..."
PRACTICES_DIR="$ROOT/practices"
if [[ ! -d "$PRACTICES_DIR" ]]; then
  fail "practices/ directory not found"
else
  shopt -s nullglob
  found_any=0
  for file in "$PRACTICES_DIR"/*.md; do
    found_any=1
    echo "  $(basename "$file")"
    require_section "$file" "^# " "H1 title"
    require_section "$file" "\*\*Trait developed:\*\*" "'Trait developed' header"
    require_section "$file" "^## Premise" "'Premise' section"
    require_section "$file" "^## The Practice" "'The Practice' section"
    require_section "$file" "^## Carry Forward" "'Carry Forward' section"
  done
  if [[ $found_any -eq 0 ]]; then
    fail "no .md files found in practices/"
  fi
fi

echo
if [[ $FAILURES -gt 0 ]]; then
  echo "$FAILURES failure(s)."
  exit 1
fi
echo "All checks passed."
