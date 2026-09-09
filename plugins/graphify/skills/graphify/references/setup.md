# Runtime setup

Upstream: [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify).
Verified 2026-09-09: revision `67f99bd0059dd1bac9e44382907ef9f10098b39f`, version `0.9.56`.
Upstream license: Apache-2.0（同梱 LICENSE-MIT・NOTICE も参照）.
The runtime is an external dependency; this marketplace does not redistribute upstream source or grant its license.

Requires Python >=3.10; verification uses Python 3.12.
Create an isolated runtime in the target workspace:

```bash
python3 -m venv .tools/graphify
.tools/graphify/bin/python -m pip install graphifyy==0.9.56
.tools/graphify/bin/graphify --help
```

Use that environment's executable in later calls.
Windows uses `.tools/graphify/Scripts/python.exe` and `graphify.exe`.
Reuse an existing verified CLI if available.
Package download contacts PyPI and its file hosting service.
Do not run `graphify install`; this marketplace already supplies the agent skill.

## Mixed documents

Code AST extraction requires no key.
Headless `extract` uses an LLM backend for document semantics.
A key existing in the environment is not authorization to send a new corpus.
Use a backend and corpus already authorized by the user.

For an authorized Gemini backend:

```bash
.tools/graphify/bin/python -m pip install 'graphifyy[gemini]==0.9.56'
.tools/graphify/bin/graphify extract <project> --backend gemini --max-concurrency 1
```

Credentials come from `GEMINI_API_KEY` or `GOOGLE_API_KEY`; never print or persist values.
This sends selected semantic material to Google's generative-language API.
Install `pdf` or `office` extras at the same version when those inputs are needed.
Other backends include local Ollama; verify its endpoint configuration before use.

For semantic extraction by the current assistant without a separate provider key, locate the upstream guide:

```bash
.tools/graphify/bin/python -c 'import graphify; from pathlib import Path; print(Path(graphify.__file__).parent / "skill-codex.md")'
```

Read its extraction/build sections and adjacent `skills/codex/references/extraction-spec.md`.
Produce the specified nodes and edges with source evidence using the current task's permitted execution mode.
Parallel subagents are optional.
Apply the extraction procedure without importing automatic upgrades, global installation, hooks, or broad query-routing rules.
Preserve corpus scope and distinguish inferred edges.
Build and inspect the resulting graph before claiming document coverage.
Extraction fragments use `edges`; exported node-link `graph.json` uses `links`.
Do not feed an exported graph back as a raw fragment without converting its edge field and preserving attributes.
Pass the same corpus root to `build_from_json` so source paths remain consistent across extraction and updates.
No MCP or paid provider is required for this host-agent path.
