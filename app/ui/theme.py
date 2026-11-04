
from __future__ import annotations

# ============================================================
# CAREERCOPILOT - DARK AURORA THEME
# ============================================================
#
# Single application theme.
# No light mode.
# No HTML or CSS injection.
# Native Streamlit theme is configured in config.toml.
# ============================================================


DARK_THEME = {
    "name": "dark",
    "background": "#050509",
    "secondary_background": "#0B0B14",
    "surface": "#101426",
    "surface_strong": "#171D35",
    "surface_hover": "#202947",
    "text": "#F8FAFC",
    "text_secondary": "#CBD5E1",
    "muted": "#94A3B8",
    "primary": "#8B5CF6",
    "accent": "#3B82F6",
    "cyan": "#22D3EE",
    "pink": "#EC4899",
    "green": "#22C55E",
    "gold": "#FBBF24",
    "red": "#F87171",
    "border": "#29324D",
    "border_hover": "#6475A5",
    "button_background": "#172449",
    "button_text": "#F8FAFC",
    "button_hover": "#25396B",
    "card_background": "#101426",
    "card_border": "#29324D",
    "shadow": "#000000",
    "glow": "#6366F1",
    "progress_background": "#1B2948",
    "progress_fill": "#22D3EE",
}


DEFAULT_THEME = "dark"


def get_theme(theme: str = DEFAULT_THEME) -> dict:
    """
    Return the single supported CareerCopilot theme.

    The argument remains for compatibility with existing
    imports. Light mode is no longer supported.
    """
    return DARK_THEME.copy()


def get_theme_value(
    key: str,
    theme: str = DEFAULT_THEME,
    fallback=None,
):
    """Return one dark-theme design token."""
    return DARK_THEME.get(key, fallback)


def load_theme() -> dict:
    """Return the default CareerCopilot theme."""
    return get_theme()
