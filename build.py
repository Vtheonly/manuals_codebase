"""CLI for compiling one JSON document or a directory of JSON documents."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from compiler import build


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compile JSON document specifications into HTML/PDF/SVG artifacts."
    )
    parser.add_argument("input", type=Path, help="JSON file or directory")
    parser.add_argument(
        "--batch",
        action="store_true",
        help="Treat input as a directory and compile every top-level .json file",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("output"),
        help="Output directory (default: ./output)",
    )
    args = parser.parse_args()

    if args.batch:
        if not args.input.is_dir():
            parser.error("--batch requires a directory")
        args.output.mkdir(parents=True, exist_ok=True)
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

    if not args.input.is_file():
        parser.error(f"Input file does not exist: {args.input}")

    manifest = build(args.input, args.output)
    print(json.dumps(manifest, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
