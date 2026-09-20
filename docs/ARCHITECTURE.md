# Architecture

## Boundary

This repository implements a **domain-agnostic renderer**.

The source/content boundary is intentionally strict:

~~~text
                  EXTERNAL INPUT
                        |
                        v
                   document.json
                        |
                        v
                    validation
                        |
                        v
                  design tokens
                        |
                        v
               semantic component tree
                        |
              +---------+---------+
              |                   |
              v                   v
        SVG artifacts         HTML document
                                  |
                                  v
                            optional PDF
                                  |
                                  v
                               manifest
~~~

The JSON document is the only source of actual content. The engine may provide visual defaults, but it cannot provide defaults for what the document means.

## Responsibilities

### JSON input

Owns all facts and composition:

- title and metadata
- language and direction
- pages and page ordering
- block ordering and nesting
- text, labels, numbers, table data
- chart and diagram data
- footer values
- optional design overrides

### Design system

core/design.py provides generic defaults for:

- palette
- typography
- spacing
- borders
- page dimensions

Overrides are read from the input JSON. Design tokens have no document-specific vocabulary.

### Components

core/components.py maps generic component types to HTML fragments.

A component may understand a semantic concept such as a table, quote, or callout. It may not assume that a table is about finance, education, manufacturing, medicine, or any other domain.

The group component allows nested component trees, so layout structure is also supplied by JSON.

### Visual artifacts

core/svg.py renders generic visual primitives.

Charts consume labels and numeric values. Labels can be simple strings or generic objects containing text and subtext. There are no language-specific field names such as title_ar or title_fr.

Diagrams support generic flow steps and generic node/edge graphs.

### HTML generator

generators/html.py is a format renderer. It:

1. reads direction and language from the input
2. turns design tokens into CSS
3. resolves page blocks
4. resolves artifact references
5. applies the requested page layout
6. emits one HTML document

It does not decide what the document says.

### PDF generator

generators/pdf.py attempts available HTML-to-PDF adapters. It is content-blind and does not contain report facts.

### Compiler

compiler.py owns:

- loading a caller-supplied JSON path
- validation
- design-system creation
- independent artifact generation
- block materialization
- HTML assembly
- optional PDF generation
- provenance and SHA-256 manifest generation

It has no default source file and no report-specific metadata.

### CLI

build.py provides single-file and batch execution. Both modes use the same compiler.

## Extensibility

New output targets should consume the same validated document model.

DOCX, Markdown, PNG, presentation, and other renderers can be added without changing the source/content contract.

New semantic components can be added as reusable primitives without introducing domain-specific fields.

## Invariant

The codebase becomes domain-specific the moment a renderer or component starts requiring or inventing fields whose meaning belongs to one particular report or application.

That is the boundary this repository must preserve.

## Text integrity & bidirectional isolation (`core/text.py`)

Every text surface passes through the ingestion pipeline:

1. **Unicode NFC normalization** of every string at load time.
2. **Arabic joining-integrity lint** that fails the build on unambiguous
   corruption (whitespace before combining marks, invisible BiDi control
   characters). The engine never guesses how to rejoin broken letters at
   render time — source data is repaired at the source.
3. **Automated bidirectional isolation**: Latin letters, digits, signed
   numbers (`+4.0`), dates (`2026`), codes and mixed French phrases
   embedded in RTL prose are wrapped in `<bdi dir="ltr">` runs. The scanner is
   tag-aware and safe for both plain values and trusted author markup.

## Measured, overflow-safe pagination (`core/paginate.py`)

Pages are never trusted to fit. The compiler renders a layout probe, measures
real Chromium geometry (per-block outer heights, flex gaps, table internals),
and reflows overflowing pages:

* Trailing blocks **flow into the next accepting page** (natural document
  flow); a page may declare `"break": true` to always start fresh.
* **Long tables split at row boundaries** with repeated column headers and
  continuous zebra striping (`_zebra_offset`), exactly like a print engine.
* **keep_with_next**: headings and subsections never strand at a page bottom.
* A single block taller than an empty page fails fast with an actionable
  error instead of silently clipping.
* TOC **`page_ref`** entries (page ids or block anchors) resolve against the
  *final* pagination, so numbers stay correct after any reflow.
* The final render is audited for residual overflow and the result is
  recorded in the manifest (`pagination` block).

## Strict data contracts (`core/validate.py`)

* Charts: non-empty labels/values/series, numeric values, matching lengths —
  ghost charts cannot build silently. Common aliases (`data`→`values`,
  `categories`→`labels`, …) are canonicalized first (`core/normalize.py`).
* TOC items require `page` or `page_ref`; unknown refs are rejected.
* `page_ref` may target a page id or any block carrying an `id` (anchor).

## PDF backend

Playwright-driven Chromium is the canonical backend (it also powers the
measurement pass, so the PDF is produced by the exact Blink layout that was
measured). Standalone Chromium and WeasyPrint remain as fallbacks for PDF
export only.
