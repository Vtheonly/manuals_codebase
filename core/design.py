"""Data-driven design tokens for the artifact engine."""
from dataclasses import asdict, dataclass, field
from typing import Any, Mapping


@dataclass(frozen=True)
class Palette:
    primary_deep: str = "#17324d"
    primary: str = "#2c5f85"
    primary_light: str = "#eef5fa"
    accent: str = "#b1782f"
    accent_light: str = "#fbf1df"
    banner_start: str = "#dbeafe"
    banner_end: str = "#f8fafc"
    banner_border: str = "#93c5fd"
    banner_text: str = "#17324d"
    text_dark: str = "#17212b"
    text: str = "#334155"
    muted: str = "#64748b"
    surface: str = "#ffffff"
    surface_alt: str = "#f8fafc"
    border: str = "#94a3b8"
    border_light: str = "#e2e8f0"
    series: tuple[str, ...] = (
        "#2c5f85",
        "#b1782f",
        "#3f7d5c",
        "#8a4f6e",
        "#6b7280",
    )


@dataclass(frozen=True)
class Typography:
    primary: str = "Arial, sans-serif"
    secondary: str = "Segoe UI, sans-serif"
    mono: str = "Consolas, monospace"
    sizes: dict[str, str] = field(default_factory=lambda: {
        "xs": "7.5pt", "sm": "8.5pt", "base": "10pt", "md": "11pt",
        "lg": "13pt", "xl": "16pt", "2xl": "20pt", "3xl": "26pt",
    })
    weights: dict[str, int] = field(default_factory=lambda: {
        "regular": 400, "medium": 500, "bold": 700, "heavy": 800, "black": 900,
    })
    line_height: dict[str, float] = field(default_factory=lambda: {
        "tight": 1.2, "normal": 1.55, "relaxed": 1.8,
    })


@dataclass(frozen=True)
class Spacing:
    page_x: str = "12mm"
    page_y: str = "10mm"
    xs: str = "4px"
    sm: str = "8px"
    md: str = "12px"
    lg: str = "18px"
    xl: str = "28px"
    card: str = "14px 18px"
    cell: str = "6px 10px"
    gap: str = "10px"
    frame_padding: str = "12mm"


@dataclass(frozen=True)
class Borders:
    thin: str = "1px"
    medium: str = "1.5px"
    thick: str = "2.5px"
    radius_sm: str = "4px"
    radius_md: str = "8px"
    radius_lg: str = "14px"
    pill: str = "999px"


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
