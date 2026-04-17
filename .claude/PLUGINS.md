# Claude Code Plugins

This repo ships with a pre-configured set of Claude Code plugins via
`.claude/settings.json`. When you open the repo in Claude Code and trust the
folder, you'll be prompted to install any missing marketplaces/plugins.

## Installed plugins

| # | Plugin              | Source                                     | Marketplace               |
|---|---------------------|--------------------------------------------|---------------------------|
| 1 | superpowers         | github.com/obra/superpowers                | claude-plugins-official   |
| 2 | frontend-design     | claude.com/plugins/frontend-design         | claude-plugins-official   |
| 3 | code-review         | claude.com/plugins/code-review             | claude-plugins-official   |
| 4 | security-guidance   | claude.com/plugins/security-guidance       | claude-plugins-official   |
| 5 | claude-mem          | github.com/thedotmack/claude-mem           | thedotmack                |
| 6 | gstack              | github.com/garrytan/gstack                 | (manual — see below)      |

### Notes

- **claude-plugins-official** is the Anthropic-managed marketplace and is
  automatically available in Claude Code — no `extraKnownMarketplaces` entry
  needed.
- **claude-mem**: the upstream repo is `thedotmack/claude-mem` (the
  `nicholasgasior/claude-mem` URL in the original request is a 404). The
  marketplace is registered in `.claude/settings.json` under the name
  `thedotmack`.
- **gstack** is **not** a Claude Code plugin — it's a standalone skill
  collection that installs to `~/.claude/skills/gstack`. Install it manually
  via:

  ```bash
  ./scripts/install_gstack.sh
  ```

  Requires `git` and `bun` (v1.0+).

## Applying changes

After the marketplaces and plugins are installed, run `/reload-plugins` in
Claude Code to activate them without restarting.
