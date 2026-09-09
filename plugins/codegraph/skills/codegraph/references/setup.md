# Runtime setup

Upstream: [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph).
Verified 2026-09-09: revision `d3f9ef9bef77a8f7a563a620df29f6eb1085d764`, version `1.6.0`.
Upstream license: MIT.
The runtime is an external dependency; this marketplace does not redistribute upstream source or grant its license.

Use the exact scoped npm package to avoid a different CodeGraph.
The source package declares Node.js >=20 and <25.
The published package includes a platform runtime selected by its launcher.

```bash
npm install --prefix .tools/codegraph @colbymchenry/codegraph@1.6.0
export PATH="$PWD/.tools/codegraph/node_modules/.bin:$PATH"
export CODEGRAPH_TELEMETRY=0
export DO_NOT_TRACK=1
codegraph --version
```

Run from the target workspace.
Reuse an existing verified CLI when available.
The PATH change is shell-local; later tool calls must resolve the launcher or re-establish PATH.
Do not edit shell startup files for a task-local install.

Installation contacts the npm registry for the package and platform dependency.
Indexing reads source and writes `.codegraph/`; review initialization prompts for additional watcher or indexing setup.
Upstream telemetry is enabled by default.
The overrides disable collection and the separate MCP update check without changing global preferences.
See upstream [TELEMETRY.md](https://github.com/colbymchenry/codegraph/blob/d3f9ef9bef77a8f7a563a620df29f6eb1085d764/TELEMETRY.md).
No API key is required.
MCP is optional upstream; this plugin uses CLI analysis and has no `.mcp.json`.
