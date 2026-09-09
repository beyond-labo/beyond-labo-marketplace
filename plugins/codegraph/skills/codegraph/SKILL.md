---
name: codegraph
description: Use colbymchenry CodeGraph to index source and inspect symbols, callers, callees, and change impact through its local CLI. Use for code structure or impact analysis; use Graphify for document-to-code knowledge graphs and Archify for presentation diagrams.
---

# Codegraph

Use `@colbymchenry/codegraph`, not another package named CodeGraph.
Read [setup.md](references/setup.md) when the runtime is missing or its identity is uncertain.

## Establish the index

Resolve the requested repository or subproject root.
Set `CODEGRAPH_TELEMETRY=0` and `DO_NOT_TRACK=1` for this workflow.
Check `codegraph --version` and `codegraph status <project> --json`.
For an unindexed project, `codegraph init <project>` builds `.codegraph/`.
Initialization may offer additional watcher or indexing setup; keep it scoped to the requested project.
Inspect help for the installed version; do not force past an unexpected root.
After source changes, run `codegraph sync <project>` and check status again.
CLI-only use has no persistent watcher; do not promise automatic freshness.

## Explore

```bash
codegraph query "<symbol>" --path <project> --json
codegraph node "<symbol>" --path <project> --file <relative-file>
codegraph callers "<symbol>" --path <project> --json
codegraph callees "<symbol>" --path <project> --json
codegraph impact "<symbol>" --path <project> --depth 2 --json
codegraph affected <changed-file> --path <project> --json
```

Resolve symbols with `query` before traversing.
Use returned file paths and supported `--file` options to disambiguate identical names.
Use `explore "<question>" --path <project>` for an unfamiliar subsystem and `context "<task>" --path <project>` for bounded implementation context.
Check help when the installed version differs.

Verify decisive findings against current source and tests.
Separate direct callers, transitive dependents, and candidate tests.
Dynamic calls, unsupported syntax, stale extraction, missing files, and truncation limit completeness.
An empty result does not establish no impact; use targeted source search when necessary.
The default test-file patterns may miss a repository's naming convention.
For Python prefix-style tests, use `codegraph affected <changed-file> --path <project> --filter 'test_*.py' --json` and verify the returned files.

## Deliver and boundaries

Report target, index status, source locations, dependency paths, and implications for the requested change.
Test candidates are not proof of safety.
The integration uses CLI commands; it does not register MCP or start a daemon.
Do not run `install`, `upgrade`, hooks, or `uninstall` to answer analysis questions: those operations can modify agent settings and other installations.
