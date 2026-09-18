"""CLI for compiling one JSON document, a JSON batch file, or a directory."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from compiler import build


def load_batch_file(path: Path) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))

    if isinstance(payload, list):
        documents = payload
    elif isinstance(payload, dict) and isinstance(payload.get("documents"), list):
        documents = payload["documents"]
    else:
        raise ValueError("Batch JSON must be an array or an object containing a 'documents' array")

    for index, document in enumerate(documents, start=1):
        if not isinstance(document, dict):
            raise ValueError(f"Batch item {index} must be an object")
    return documents


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compile JSON document specifications into HTML/PDF/SVG artifacts."
    )
    parser.add_argument("input", type=Path, help="JSON file or directory")
    parser.add_argument(
        "--batch",
        action="store_true",
        help="Treat input as a directory or batch JSON file",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("output"),
        help="Output directory (default: ./output)",
    )
    args = parser.parse_args()

    if args.batch:
        args.output.mkdir(parents=True, exist_ok=True)

        if args.input.is_dir():
            files = sorted(args.input.glob("*.json"))
            if not files:
                parser.error(f"No JSON files found in {args.input}")
            for source in files:
                target = args.output / source.stem
                manifest = build(source, target)
                print(
                    f"Built {source.name}: "
                    f"{len(manifest['artifacts'])} artifacts, "
                    f"PDF={manifest['outputs']['pdf']['generated']}"
                )
            return 0

        if args.input.is_file():
            try:
                documents = load_batch_file(args.input)
            except (OSError, json.JSONDecodeError, ValueError) as exc:
                parser.error(str(exc))

            from tempfile import TemporaryDirectory

            with TemporaryDirectory() as temp_dir:
                temp_root = Path(temp_dir)
                for index, document in enumerate(documents, start=1):
                    document_id = str(document.get("id", f"document-{index}"))
                    source = temp_root / f"{args.input.stem}-{index:03d}-{document_id}.json"
                    source.write_text(
                        json.dumps(document, ensure_ascii=False, indent=2),
                        encoding="utf-8",
                    )
                    target = args.output / f"{index:03d}-{document_id}"
                    manifest = build(source, target)
                    print(
                        f"Built batch item {index} ({document_id}): "
                        f"{len(manifest['artifacts'])} artifacts, "
                        f"PDF={manifest['outputs']['pdf']['generated']}"
                    )
            return 0

        parser.error(f"Input does not exist: {args.input}")

    if not args.input.is_file():
        parser.error(f"Input file does not exist: {args.input}")

    manifest = build(args.input, args.output)
    print(json.dumps(manifest, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
