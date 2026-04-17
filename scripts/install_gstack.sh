#!/usr/bin/env bash
# Install gstack skills system (github.com/garrytan/gstack)
#
# gstack is NOT a Claude Code plugin — it is a standalone skill collection
# that installs to ~/.claude/skills/gstack. Unlike the plugins configured in
# .claude/settings.json, it must be installed per-user via this script.
#
# Requirements: git, bun (v1.0+), node.js (Windows only)

set -euo pipefail

GSTACK_DIR="${HOME}/.claude/skills/gstack"

if [ -d "${GSTACK_DIR}" ]; then
  echo "gstack already installed at ${GSTACK_DIR}"
  echo "To update: cd ${GSTACK_DIR} && git pull && ./setup"
  exit 0
fi

echo "Cloning gstack into ${GSTACK_DIR}..."
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git "${GSTACK_DIR}"

echo "Running gstack setup..."
cd "${GSTACK_DIR}"
./setup

echo ""
echo "gstack installed. Add a 'gstack' section to your CLAUDE.md listing the skills you want to use."
echo "See https://github.com/garrytan/gstack for available commands (e.g. /office-hours, /review, /qa, /ship)."
