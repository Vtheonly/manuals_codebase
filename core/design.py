"""
core/design.py — Abstract Design Tokens with JSON Theme Overrides
Single source of truth for Palette, Typography, Spacing, Borders, and Page Geometry.

All values are generic visual defaults. A JSON document may override any token
through its `theme` block; unknown token names are rejected.
"""
from dataclasses import asdict, dataclass, field
from typing import Any, Mapping


@dataclass(frozen=True)
class Palette:
    primary: str = "#1e4b7a"
    primary_deep: str = "#0f2d4a"
    primary_light: str = "#eef4fb"

    accent: str = "#c2932e"
    accent_text: str = "#a87b2d"
    accent_light: str = "#faf5e6"

    banner_start: str = "#8dbce9"
    banner_end: str = "#a2cbf8"
    banner_border: str = "#6ba3dc"
    banner_text: str = "#0f2d4a"

    series: tuple[str, ...] = (
        "#2d6494",
        "#c2932e",
        "#7ba3c4",
        "#0f2d4a",
        "#94a3b8",
    )

    text_dark: str = "#0f2d4a"
    text: str = "#1f2937"
    muted: str = "#6b7280"
    muted_light: str = "#94a3b8"
    surface: str = "#ffffff"
    surface_alt: str = "#eef4fb"
    surface_warm: str = "#f7f6f2"
    border: str = "#cbd5e1"
    border_light: str = "#e3e9f1"
    border_table: str = "#d7dfe8"
    border_table_strong: str = "#b9c6d6"
    dots: str = "#dbe3ec"
    divider_strong: str = "#7ba3c4"
    frame_inner: str = "#79b3ee"
    back_cover: str = "#0f2d4a"
    back_frame: str = "#d4b36a"
    chart_axis: str = "#3b4a5c"
    chart_track: str = "#edf1f6"
    chart_track_border: str = "#7ba3c4"


@dataclass(frozen=True)
class Typography:
    families: dict[str, str] = field(default_factory=lambda: {
        "arabic": "'Noto Kufi Arabic', 'Noto Sans Arabic UI', 'Cairo', 'Segoe UI', Tahoma, sans-serif",
        "latin": "'Arimo', 'Inter', 'Segoe UI', Arial, 'Noto Kufi Arabic', sans-serif",
        "math": "'Tinos', 'Cambria Math', 'Latin Modern Math', 'Times New Roman', 'Noto Kufi Arabic', serif",
        "quote": "'Amiri', 'Noto Naskh Arabic', 'Traditional Arabic', serif",
        "chart_arabic": "'Noto Sans Arabic UI', 'Noto Kufi Arabic', sans-serif",
        "chart_latin": "'Tinos', 'Arimo', 'Times New Roman', 'Noto Kufi Arabic', serif",
    })
    sizes: dict[str, str] = field(default_factory=lambda: {
        "2xs": "6pt",
        "xs": "7pt",
        "sm": "8pt",
        "base": "8.5pt",
        "md": "9pt",
        "lg": "10pt",
        "xl": "10.5pt",
        "2xl": "11.5pt",
        "3xl": "13.5pt",
        "4xl": "15pt",
        "5xl": "17pt",
        "6xl": "19pt",
    })
    weights: dict[str, int] = field(default_factory=lambda: {
        "regular": 400,
        "medium": 500,
        "semibold": 600,
        "bold": 700,
        "heavy": 800,
        "black": 900,
    })
    line_height: dict[str, float] = field(default_factory=lambda: {
        "tight": 1.3,
        "normal": 1.45,
        "relaxed": 1.65,
        "loose": 1.88,
    })


@dataclass(frozen=True)
class Spacing:
    page_x: str = "14.75mm"
    page_y: str = "15.9mm"
    page_bottom: str = "50.8mm"
    xs: str = "4px"
    sm: str = "8px"
    md: str = "12px"
    lg: str = "18px"
    xl: str = "28px"
    card: str = "14px 20px"
    cell: str = "6px 10px"
    gap: str = "10px"
    frame_padding: str = "12mm 14mm"


@dataclass(frozen=True)
class Borders:
    thin: str = "0.75px"
    medium: str = "1px"
    thick: str = "1.5px"
    heavy: str = "2.25px"
    radius_sm: str = "4px"
    radius_md: str = "6px"
    radius_lg: str = "8px"
    radius_xl: str = "12px"
    pill: str = "30px"
    rule_overlay: str = "96pt"


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
