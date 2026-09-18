from typing import Any, Dict, Iterable

REQUIRED_REPORT = ("id", "title", "language", "sections", "artifacts")

def validate(source: Dict[str, Any]) -> None:
    missing = [k for k in REQUIRED_REPORT if k not in source]
    if missing:
        raise ValueError(f"Missing report fields: {', '.join(missing)}")
    ids = set()
    for artifact in source["artifacts"]:
        for key in ("id", "type"):
            if key not in artifact:
                raise ValueError(f"Artifact missing '{key}'")
        if artifact["id"] in ids:
            raise ValueError(f"Duplicate artifact id: {artifact['id']}")
        ids.add(artifact["id"])
        if artifact["type"] == "chart":
            if len(artifact.get("labels", [])) != len(artifact.get("values", [])):
                raise ValueError(f"Chart {artifact['id']} labels/values length mismatch")
        if artifact["type"] == "diagram":
            n = len(artifact.get("nodes", []))
            for edge in artifact.get("edges", []):
                if len(edge) != 2 or not all(isinstance(x, int) and 0 <= x < n for x in edge):
                    raise ValueError(f"Invalid edge in diagram {artifact['id']}")
