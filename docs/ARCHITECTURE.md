# Architecture

## Canonical pipeline

`Source Data → Validated Model → Semantic Components → Artifact Generators → Final Outputs`

1. Load the single source document.
2. Validate schema and artifact IDs.
3. Resolve semantic components.
4. Render every visual artifact independently.
5. Render every content block independently.
6. Compose the independently generated pieces into HTML.
7. Convert the composed HTML to PDF.
8. Emit a generated Python representation of the source.
9. Hash every generated artifact and write a manifest.

## Separation of concerns

- **Source:** facts, text, labels, values, relationships and ordering.
- **Design:** typography, font fallback, weights, italics, underline semantics, spacing, borders, radius, palette, semantic colors, page geometry and visual rules.
- **Components:** semantic concepts such as heading, body, quote, table and callout.
- **Generators:** format-specific rendering adapters.
- **Compiler:** orchestration, validation, regeneration and provenance.

No renderer should contain report-specific facts.

## Centralized design domains

Typography, spacing, borders, colors, numbers, quotes, lists, tables, callouts, code, diagrams, charts, images/illustrations, page/layout, hierarchy and accessibility metadata should be represented as design tokens or semantic component rules.

## Determinism

The source is hashed before generation. Every generated artifact is hashed after generation. The manifest records the source hash, generator version, artifact IDs, output paths and output hashes.

Fonts should be bundled in production when byte-level cross-machine visual consistency is required. The current sample deliberately avoids runtime font downloads.

## Extension path

The architecture is intentionally renderer-neutral. Future targets can add DOCX, Markdown, PNG, presentation slides or web output without changing the source model.
