---
name: archify
description: Generate validated architecture, workflow, sequence, data-flow, or lifecycle diagrams as standalone HTML with Archify. Use for diagram creation from descriptions, code evidence, or Mermaid, not architecture reviews without a diagram deliverable.
---

# Archify

Use tt-a1i/archify to produce editable JSON and standalone HTML.
Read [setup.md](references/setup.md) when the upstream runtime is missing.
This integration guide does not bundle the renderer.

## Author

Resolve the installed checkout and verify its recorded revision.
Choose `architecture` for components, `workflow` for processes, `sequence` for messages, `dataflow` for data movement, or `lifecycle` for states.
Read the selected schema, `schemas/common.schema.json`, and one matching JSON example inside the upstream `archify/` directory.
Use the schema for field names instead of guessing.

When the diagram represents existing code, inspect source evidence and distinguish observed relationships from proposed changes.
Start with stable IDs, a clear primary path, and meaningful directional labels.
Use `meta.quality_profile: "showcase"` for presentation output.
Preserve topology when translating Mermaid into typed JSON; the renderer does not consume Mermaid directly.
Japanese authored labels are supported; omit `meta.locale` for Japanese and disclose that fixed viewer controls remain English.

## Validate and deliver

Run from the upstream `archify/` directory, resolving artifact paths relative to that directory.

```bash
node bin/archify.mjs validate <type> <diagram.json> --quality showcase --json
node bin/archify.mjs deliver <type> <diagram.json> <diagram.html> --quality showcase --json
```

Repair diagnosed subjects using the returned evidence and supported fixes.
Read upstream `references/authoring-contract.md` for geometry or field details.
Preserve meaningful labels when fixing overlaps.
If two consecutive corrections do not improve the error count, report unresolved diagnostics.
Failed delivery can preserve an older output; never present that file as the successful new result.

Inspect the exact delivered HTML in an available browser for clipping, labels, crossings, and requested interactions.
Read upstream `references/delivery-contract.md` for optional `visual-check` and exports.
Report deterministic validation separately from browser inspection and disclose unavailable checks.
Return both JSON and HTML links.
Preview and motion are optional modes; use them when requested.

## Boundaries

System Architecture Design owns design decisions and reviews.
Graphify and CodeGraph can supply extracted evidence but are not required to draw a described system.
Diagram validation does not establish that a system description is true.
Do not install other agent skills, hooks, or MCP servers to render a diagram.
