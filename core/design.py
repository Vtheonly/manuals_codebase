"""
core/design.py — Centralized Design System Tokens
"""
from dataclasses import dataclass, field
from typing import Dict, Tuple

@dataclass(frozen=True)
class Palette:
    # الألوان الأساسية
    primary_deep: str = "#0c2340"       # كحلي داكن ملكي للغلاف الخلفي والعناوين
    primary: str = "#1e4b7a"            # أزرق رسمي للمؤسسة والإطارات وترويسات الجداول
    primary_light: str = "#eef4fb"      # خلفية خفيفة للتنبيهات والصفوف المتبادلة
    accent: str = "#c28b2e"             # ذهبي نحاسي للمخططات والشارات
    accent_light: str = "#fef3c7"       # خلفية التنبيهات الذهبية
    
    # بطاقة عنوان التقرير (Gradient Box)
    banner_start: str = "#8cbbe8"
    banner_end: str = "#a4cdfa"
    banner_border: str = "#6ba3dc"
    banner_text: str = "#0c2d48"
    
    # سلاسل الرسوم البيانية المتناوبة
    series: Tuple[str, ...] = ("#1e4b7a", "#c28b2e", "#2b7a5a", "#a33b3b", "#6b7280")
    
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
    arabic: str = "'Cairo', sans-serif"
    latin: str = "'Inter', 'Segoe UI', sans-serif"
    code: str = "'Courier New', monospace"
    sizes: Dict[str, str] = field(default_factory=lambda: {
        "xs": "7.5pt", "sm": "8.5pt", "base": "10pt", "md": "11pt",
        "lg": "13pt", "xl": "15pt", "2xl": "18pt", "3xl": "24pt"
    })
    weights: Dict[str, int] = field(default_factory=lambda: {
        "regular": 400, "medium": 500, "bold": 700, "heavy": 800, "black": 900
    })
    line_height: Dict[str, float] = field(default_factory=lambda: {
        "tight": 1.25, "normal": 1.65, "relaxed": 1.85
    })

@dataclass(frozen=True)
class Spacing:
    page_x: str = "12mm"
    page_y: str = "10mm"
    frame_padding: str = "10mm 12mm"
    card: str = "14px 20px"
    cell: str = "6px 10px"

@dataclass(frozen=True)
class Borders:
    frame_width: str = "2.5px"
    radius_sm: str = "4px"
    radius_md: str = "8px"
    radius_lg: str = "14px"
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

DESIGN = DesignSystem()