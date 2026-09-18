from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

@dataclass(frozen=True)
class Text:
    id: str
    value: str
    role: str = "body"
    lang: str = "ar"
    emphasis: List[str] = field(default_factory=list)

@dataclass(frozen=True)
class Table:
    id: str
    title: str
    columns: List[str]
    rows: List[List[Any]]

@dataclass(frozen=True)
class Chart:
    id: str
    kind: str
    title: str
    labels: List[str]
    values: List[float]
    unit: str = ""

@dataclass(frozen=True)
class Diagram:
    id: str
    title: str
    nodes: List[str]
    edges: List[List[int]]

@dataclass(frozen=True)
class Section:
    id: str
    title: str
    blocks: List[Dict[str, Any]]

@dataclass(frozen=True)
class Report:
    id: str
    title: str
    language: str
    metadata: Dict[str, Any]
    sections: List[Section]
    artifacts: List[Dict[str, Any]]
