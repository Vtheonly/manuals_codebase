from dataclasses import dataclass, field
from typing import Dict, Tuple

@dataclass(frozen=True)
class Palette:
    primary: str = "#1e4b7a"
    primary_deep: str = "#0c2340"
    primary_light: str = "#eef4fb"
    accent: str = "#b45309"
    accent_light: str = "#fef3c7"
    text: str = "#1e293b"
    text_dark: str = "#0f172a"
    muted: str = "#64748b"
    surface: str = "#ffffff"
    surface_alt: str = "#f8fafc"
    border: str = "#94a3b8"
    border_light: str = "#e2e8f0"
    series: Tuple[str, ...] = ("#1e4b7a", "#c28b2e", "#2b7a5a", "#a33b3b", "#6b7280")

@dataclass(frozen=True)
class Typography:
    arabic: str = "Cairo, Arial, sans-serif"
    latin: str = "Inter, Segoe UI, sans-serif"
    code: str = "Courier New, monospace"
    sizes: Dict[str, str] = field(default_factory=lambda: {
        "xs":"8pt","sm":"9pt","base":"10pt","md":"12pt","lg":"14pt",
        "xl":"18pt","2xl":"22pt","3xl":"28pt"
    })
    weights: Dict[str, int] = field(default_factory=lambda: {
        "regular":400,"medium":500,"bold":700,"heavy":800,"black":900
    })
    line_height: Dict[str, float] = field(default_factory=lambda: {
        "tight":1.25,"normal":1.6,"relaxed":1.85
    })

@dataclass(frozen=True)
class Spacing:
    page_x: str = "14mm"
    page_y: str = "12mm"
    xs: str = "4px"
    sm: str = "8px"
    md: str = "14px"
    lg: str = "20px"
    xl: str = "32px"
    card: str = "14px 18px"
    cell: str = "6px 10px"

@dataclass(frozen=True)
class Borders:
    thin: str = "1px"
    medium: str = "1.5px"
    thick: str = "2.5px"
    sm: str = "4px"
    md: str = "8px"
    lg: str = "14px"
    pill: str = "999px"

@dataclass(frozen=True)
class Page:
    width: str = "210mm"
    height: str = "297mm"
    margin: str = "0"

@dataclass(frozen=True)
class DesignSystem:
    palette: Palette = field(default_factory=Palette)
    typography: Typography = field(default_factory=Typography)
    spacing: Spacing = field(default_factory=Spacing)
    borders: Borders = field(default_factory=Borders)
    page: Page = field(default_factory=Page)

DESIGN = DesignSystem()
