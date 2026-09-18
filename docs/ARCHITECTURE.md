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
