# Manuals Codebase — Centralized Artifact Engine

A from-scratch, deterministic artifact/document generation system.

## Architecture

`Source Data → Validated Structured Model → Semantic Components → Artifact Generators → Manifested Outputs`

The source describes **what** exists. Design tokens describe **how** it looks. Semantic components describe **what kind of artifact** it is. Generators decide **how to render it** for a target format.

## Guarantees

- One canonical JSON source per report.
- One centralized design system consumed by every renderer.
- Every artifact has a stable ID and is generated independently.
- SVG charts/diagrams are deterministic and dependency-free.
- HTML is always generated; PDF is generated when ReportLab is installed.
- A manifest records every output, SHA-256 hash, source hash, and generator version.
- Validation happens before rendering.
- No generator is allowed to invent report content.

## Layout

```text
manuals_codebase/
├── core/
│   ├── design.py
│   ├── model.py
│   ├── validate.py
│   ├── svg.py
│   └── components.py
├── generators/
│   ├── html.py
│   └── pdf.py
├── source/
│   └── report.json
├── output/
├── compiler.py
├── build.py
├── requirements.txt
└── tests/
    └── test_engine.py
```

## Run

```bash
python build.py
```

The build creates one output directory containing the final HTML, PDF when available, individual SVG artifacts, generated Python source representation, and a deterministic manifest.

## Design principle

Never style an artifact directly inside a generator. Renderers consume semantic components and design tokens. This makes a visual change a single-source change instead of a project-wide patch.
