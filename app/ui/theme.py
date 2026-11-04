
from __future__ import annotations


# ============================================================
# CAREERCOPILOT DESIGN SYSTEM
# ============================================================
#
# Native Python theme tokens.
#
# No HTML.
# No unsafe_allow_html.
# No JavaScript.
#
# Existing theme functions are preserved.
# ============================================================


DARK_THEME = {
    "name": "dark",

    # Backgrounds
    "background": "#030511",
    "secondary_background": "#080D20",
    "surface": "#0C1530",
    "surface_strong": "#101D3B",
    "surface_hover": "#16264A",

    # Typography
    "text": "#F7F9FF",
    "text_secondary": "#C1CCE0",
    "muted": "#8998B5",

    # Brand colours
    "primary": "#8B5CF6",
    "accent": "#3B82F6",
    "cyan": "#22D3EE",
    "pink": "#EC4899",
    "green": "#22C55E",
    "gold": "#FBBF24",
    "red": "#F87171",

    # Borders
    "border": "#243454",
    "border_hover": "#6475A5",

    # Interactive states
    "button_background": "#172449",
    "button_text": "#F8FAFC",
    "button_hover": "#25396B",
    "button_glow": "#8B5CF6",

    # Cards
    "card_background": "#0C1530",
    "card_border": "#243454",

    # Effects
    "shadow": "#000000",
    "glow": "#6366F1",

    # Progress
    "progress_background": "#1B2948",
    "progress_fill": "#22D3EE",
}


LIGHT_THEME = {
    "name": "light",

    # Backgrounds
    "background": "#F8FAFF",
    "secondary_background": "#EEF3FF",
    "surface": "#FFFFFF",
    "surface_strong": "#F3F6FF",
    "surface_hover": "#E9EEFF",

    # Typography
    "text": "#151B35",
    "text_secondary": "#394663",
    "muted": "#68748E",

    # Brand colours
    "primary": "#7C3AED",
    "accent": "#2563EB",
    "cyan": "#0891B2",
    "pink": "#DB2777",
    "green": "#15803D",
    "gold": "#B45309",
    "red": "#DC2626",

    # Borders
    "border": "#DCE3F5",
    "border_hover": "#A5B4FC",

    # Interactive states
    "button_background": "#EDE9FE",
    "button_text": "#31205E",
    "button_hover": "#DDD6FE",
    "button_glow": "#8B5CF6",

    # Cards
    "card_background": "#FFFFFF",
    "card_border": "#E0E7F7",

    # Effects
    "shadow": "#64748B",
    "glow": "#A78BFA",

    # Progress
    "progress_background": "#E2E8F0",
    "progress_fill": "#2563EB",
}


# ============================================================
# THEME REGISTRY
# ============================================================

THEMES = {
    "dark": DARK_THEME,
    "light": LIGHT_THEME,
}


SUPPORTED_THEMES = tuple(THEMES.keys())

DEFAULT_THEME = "dark"


# ============================================================
# GET THEME
# ============================================================

def get_theme(theme: str = DEFAULT_THEME) -> dict:
    """
    Return a copy of the selected theme tokens.

    Unknown theme names safely fall back to dark mode.
    """

    selected_theme = theme.lower().strip()

    if selected_theme not in THEMES:
        selected_theme = DEFAULT_THEME

    return THEMES[selected_theme].copy()


# ============================================================
# GET THEME VALUE
# ============================================================

def get_theme_value(
    key: str,
    theme: str = DEFAULT_THEME,
    fallback: str | None = None,
) -> str | None:
    """
    Retrieve an individual design token.
    """

    tokens = get_theme(theme)

    return tokens.get(key, fallback)


# ============================================================
# LOAD DEFAULT THEME
# ============================================================

def load_theme() -> dict:
    """
    Compatibility helper used by app.py.

    Keeps dark mode as the initial default.
    """

    return get_theme(DEFAULT_THEME)


# ============================================================
# AVAILABLE THEMES
# ============================================================

def get_available_themes() -> tuple[str, ...]:
    """
    Return all supported theme names.
    """

    return SUPPORTED_THEMES
