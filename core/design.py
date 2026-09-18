"""
core/design.py — Abstract Design Tokens with JSON Theme Overrides
Single source of truth for Palette, Typography, Spacing, Borders, and Page Geometry.
"""
from dataclasses import asdict, dataclass, field
from typing import Any, Mapping


@dataclass(frozen=True)
class Palette:
    primary: str = "#1a3a5f"
    primary_deep: str = "#0d2238"
    primary_light: str = "#ebf5fb"
    accent: str = "#d35400"
    accent_gold: str = "#c5a059"
    accent_light: str = "#fff9e6"

    banner_start: str = "#72a4d4"
    banner_end: str = "#5b92e5"
    banner_border: str = "#4a7bb0"
    banner_text: str = "#ffffff"

    series: tuple[str, ...] = (
        "#2980b9",
        "#d35400",
        "#27ae60",
        "#8e44ad",
        "#1a3a5f",
    )

    text_dark: str = "#0d2238"
    text: str = "#1e293b"
    muted: str = "#718096"
    surface: str = "#ffffff"
    surface_alt: str = "#f8fafc"
    border: str = "#cbd5e1"
    border_light: str = "#e2e8f0"


@dataclass(frozen=True)
class Typography:
    font_arabic: str = "'Cairo', 'Amiri', 'Traditional Arabic', 'Scheherazade New', 'Segoe UI', Tahoma, sans-serif"
    font_latin: str = "'Inter', 'Segoe UI', Arial, sans-serif"
    font_math: str = "'Cambria Math', 'Latin Modern Math', 'Times New Roman', serif"
    sizes: dict[str, str] = field(default_factory=lambda: {
        "xs": "8pt",
        "sm": "8.5pt",
        "base": "10pt",
        "md": "11pt",
        "lg": "13pt",
        "xl": "15pt",
        "2xl": "18pt",
        "3xl": "22pt",
    })
    weights: dict[str, int] = field(default_factory=lambda: {
        "regular": 400,
        "medium": 500,
        "bold": 700,
        "heavy": 800,
        "black": 900,
    })
    line_height: dict[str, float] = field(default_factory=lambda: {
        "tight": 1.25,
        "normal": 1.65,
        "relaxed": 1.85,
    })


@dataclass(frozen=True)
class Spacing:
    page_x: str = "15mm"
    page_y: str = "14mm"
    xs: str = "4px"
    sm: str = "8px"
    md: str = "12px"
    lg: str = "18px"
    xl: str = "28px"
    card: str = "14px 20px"
    cell: str = "6px 10px"
    gap: str = "10px"
    frame_padding: str = "10mm 12mm"


@dataclass(frozen=True)
class Borders:
    thin: str = "1px"
    medium: str = "1.5px"
    thick: str = "2px"
    radius_sm: str = "4px"
    radius_md: str = "8px"
    radius_lg: str = "12px"
    pill: str = "30px"


@dataclass(frozen=True)
class Page:
    width: str = "210mm"
    height: str = "297mm"


@dataclass(frozen=True)
class DesignSystem:
    palette: Palette = field(default_factory=Palette)
    typography: Typography = field(default_factory=Typography)
    spacing: Spacing = field(default_factory=Spacing)
    borders: Borders = field(default_factory=Borders)
    page: Page = field(default_factory=Page)

    @classmethod
    def from_mapping(cls, overrides: Mapping[str, Any] | None = None) -> "DesignSystem":
        data = asdict(cls())
        merge_mapping(data, overrides or {})
        data["palette"]["series"] = tuple(data["palette"]["series"])
        return cls(
            palette=Palette(**data["palette"]),
            typography=Typography(**data["typography"]),
            spacing=Spacing(**data["spacing"]),
            borders=Borders(**data["borders"]),
            page=Page(**data["page"]),
        )


def merge_mapping(target: dict[str, Any], overrides: Mapping[str, Any]) -> None:
    for key, value in overrides.items():
        if key not in target:
            raise ValueError(f"Unknown design token group or token: {key}")
        if isinstance(value, Mapping) and isinstance(target[key], dict):
            for nested_key, nested_value in value.items():
                if nested_key not in target[key]:
                    raise ValueError(f"Unknown design token: {key}.{nested_key}")
                target[key][nested_key] = nested_value
        else:
            target[key] = value