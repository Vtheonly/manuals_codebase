"""
core/design.py — Abstract Design Tokens with JSON Theme Overrides
Single source of truth for Palette, Typography, Spacing, Borders, and Page Geometry.
"""
from dataclasses import asdict, dataclass, field
from typing import Any, Mapping


@dataclass(frozen=True)
class Palette:
    # الألوان السيادية والرسمية
    primary: str = "#1e4b7a"
    primary_deep: str = "#0c2340"
    primary_light: str = "#eef4fb"
    accent: str = "#c28b2e"
    accent_light: str = "#fef9ed"

    # بطاقة عنوان التقرير المتدرجة (Gradient Card)
    banner_start: str = "#8cbbe8"
    banner_end: str = "#a4cdfa"
    banner_border: str = "#6ba3dc"
    banner_text: str = "#0c2d48"

    # ألوان السلاسل البيانية المتطابقة
    series: tuple[str, ...] = (
        "#1e4b7a",
        "#c28b2e",
        "#2b7a5a",
        "#8a4f6e",
        "#475569",
    )

    # ألوان النصوص والمحايدات
    text_dark: str = "#0f172a"
    text: str = "#1e293b"
    muted: str = "#64748b"
    surface: str = "#ffffff"
    surface_alt: str = "#f8fafc"
    border: str = "#94a3b8"
    border_light: str = "#e2e8f0"


@dataclass(frozen=True)
class Typography:
    font_arabic: str = "'Cairo', sans-serif"
    font_latin: str = "'Inter', 'Segoe UI', sans-serif"
    font_math: str = "'Cambria Math', 'Times New Roman', serif"
    sizes: dict[str, str] = field(default_factory=lambda: {
        "xs": "7.5pt",
        "sm": "8.5pt",
        "base": "9.5pt",
        "md": "11pt",
        "lg": "13pt",
        "xl": "15pt",
        "2xl": "17pt",
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
    page_x: str = "14mm"
    page_y: str = "12mm"
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
    thick: str = "2.5px"
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