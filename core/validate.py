"""
core/validate.py — Schema Validation
"""
from typing import Any, Dict

REQUIRED_REPORT = ("id", "title", "language", "sections", "artifacts")

def validate(source: Dict[str, Any]) -> None:
    missing = [k for k in REQUIRED_REPORT if k not in source]
    if missing:
        raise ValueError(f"Missing report fields: {', '.join(missing)}")
        
    ids = set()
    for artifact in source.get("artifacts", []):
        for key in ("id", "type"):
            if key not in artifact:
                raise ValueError(f"Artifact missing '{key}'")
        if artifact["id"] in ids:
            raise ValueError(f"Duplicate artifact id: {artifact['id']}")
        ids.add(artifact["id"])