---
name: graphify
description: Build or query Graphify knowledge graphs across code, documentation, papers, and project materials. Use for cross-document relationships or explicit Graphify requests; use CodeGraph for symbol call and impact analysis and Archify for authored diagrams.
---

# Graphify

Use Graphify-Labs/graphify: its Python distribution is `graphifyy`, while the CLI is `graphify`.
Read [setup.md](references/setup.md) for first use and semantic extraction choices.
This integration uses the CLI without registering upstream hooks or MCP.

## Scope and extract

Resolve the corpus and output root.
Reuse a matching `graphify-out/graph.json` for questions when its scope and freshness are adequate.
Check manifests and source changes; an existing graph may represent a different corpus.
For a new code-only graph:

```bash
graphify extract <project> --code-only --no-cluster --max-workers 1
```

This writes raw data under `<project>/graphify-out/`.
Use `--out <output-root>` when output should live elsewhere.
Respect `.graphifyignore` and Git ignore rules.
Do not scan unrelated folders or databases.

For mixed corpora, follow the semantic path in the setup reference.
Do not substitute code-only output for requested document coverage.
Report unsupported files and extraction failures.

## Query and verify

```bash
graphify query "<question>" --graph <output-root>/graphify-out/graph.json
graphify explain "<node>" --graph <output-root>/graphify-out/graph.json
graphify path "<node-A>" "<node-B>" --graph <output-root>/graphify-out/graph.json
```

Resolve node names from results before tracing paths.
Check source evidence and distinguish extracted, inferred, and ambiguous edges.
A graph path is not necessarily a runtime execution path.
An absent edge does not prove that a relationship is absent.
Use supported query budget options to bound output.

For communities, HTML, and a report:

```bash
graphify cluster-only <output-root> --graph <output-root>/graphify-out/graph.json --no-label
```

`--no-label` avoids automatic LLM community naming.
Raw `--no-cluster` extraction alone does not create visualization or a report.
Verify generated files before linking them.
After source edits, repeat extraction with the same mode and scope; preserve document evidence and inspect shrink warnings instead of forcing overwrite.

## Deliver and boundaries

Return the graph location, corpus coverage, evidence-backed answers, and actual generated report/HTML.
Use Archify when the user wants a curated explanatory diagram.
Do not run `graphify install`, hooks, watchers, global merges, provider setup, or remote exports unless requested.
