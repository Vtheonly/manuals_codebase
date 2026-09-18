# Manuals Codebase — Generic JSON Artifact Engine

This repository is an **artifact-generation engine**, not a report implementation.

The central contract is:

**Python code = reusable tools, semantic components, renderers, design tokens, validation, and compilation infrastructure.**

**JSON input = the actual document content, data, structure, page composition, artifact specifications, language, direction, and optional theme overrides.**

The engine has no knowledge of a particular organization, report subject, person, industry, language, or expected final document.

## Pipeline

~~~text
JSON input
   ↓
validation
   ↓
design system
   ↓
semantic component tree
   ↓
visual artifacts
   ↓
HTML
   ↓
optional PDF
   ↓
manifest
~~~

The engine does not invent missing report facts. It renders what the input specifies.

## What belongs where

| Layer | Owns | Must not own |
| --- | --- | --- |
| JSON input | Text, numbers, tables, labels, pages, ordering, layout choices, artifact specs, metadata | — |
| core/design.py | Generic visual defaults and JSON theme overrides | Domain facts |
| core/components.py | Reusable semantic blocks | Document-specific fields |
| core/svg.py | Generic charts and diagrams | Domain interpretation |
| generators/ | Target-format rendering | Report content |
| compiler.py | Loading, validation, orchestration, hashing, output manifests | A default report |
| build.py | CLI and batch execution | A default source path |

## No hidden default document

There is deliberately no default source file, no hardcoded cover page, no hardcoded table of contents, no domain-specific metadata model, and no generated Python copy of the input.

A caller supplies the input:

~~~bash
python build.py path/to/document.json
~~~

Batch mode accepts either a directory of JSON documents or a **single batch JSON file**:

~~~bash
python build.py --batch path/to/json-directory
python build.py --batch path/to/batch.json
~~~

A batch JSON file can be either an array of document objects or an object containing a `documents` array.

Output can be redirected:

~~~bash
python build.py path/to/document.json --output output/my-document
~~~

## JSON structure

A document is assembled from generic pages and blocks:

~~~json
{
  "id": "document-001",
  "title": "A title supplied by the caller",
  "language": "en",
  "direction": "ltr",
  "theme": {
    "palette": {
      "primary": "#22577a",
      "accent": "#e09f3e"
    }
  },
  "pages": [
    {
      "id": "page-1",
      "layout": "standard",
      "footer": {
        "left": "Caller data",
        "center": "{page}/{pages}",
        "right": "Caller data"
      },
      "blocks": [
        {
          "type": "heading",
          "level": 1,
          "title": "Caller-defined heading"
        },
        {
          "type": "text",
          "content": "Caller-defined text"
        },
        {
          "type": "artifact_ref",
          "artifact_id": "chart-1"
        }
      ]
    }
  ],
  "artifacts": [
    {
      "id": "chart-1",
      "type": "chart",
      "kind": "bar",
      "title": "Caller-defined chart",
      "labels": ["A", "B", "C"],
      "values": [10, 20, 15]
    }
  ]
}
~~~

A batch file can use:

~~~json
{
  "documents": [
    {
      "id": "document-001",
      "title": "First document",
      "language": "en",
      "direction": "ltr",
      "pages": [],
      "artifacts": []
    },
    {
      "id": "document-002",
      "title": "Second document",
      "language": "en",
      "direction": "ltr",
      "pages": [],
      "artifacts": []
    }
  ]
}
~~~

Supported generic block primitives include headings, text, badges, cards, key/value cards, callouts, statistics, tables, flow steps, tables of contents, quotes, lists, groups, images, spacers, and artifact references.

Supported visual artifacts include bar, line, donut, and progress charts plus flow and graph diagrams.

Nested groups make page structure declarative. The input decides which components exist and in what order; the engine only supplies their reusable rendering behavior.

## Examples

The examples directory contains **non-runtime demonstration inputs only**. They exist to prove that materially different JSON documents can use the same engine.

They are never imported by the compiler and never determine engine defaults.

## Determinism and provenance

The compiler records:

- input filename
- input SHA-256
- engine version
- every generated artifact ID
- every generated artifact hash
- HTML output hash
- optional PDF status/hash

Visual artifacts are generated independently before the document is assembled.

## PDF

HTML is the primary guaranteed output. PDF generation is opportunistic through WeasyPrint, Chromium, or Playwright when one is available in the environment.

No PDF backend is allowed to invent or substitute document content.

## Design overrides

All design defaults are generic. A caller may override palette, typography, spacing, borders, or page dimensions in JSON.

Unknown design token names are rejected so spelling mistakes do not silently change rendering.
