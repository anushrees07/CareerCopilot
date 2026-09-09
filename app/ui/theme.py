from __future__ import annotations


# ============================================================
# CAREERCOPILOT THEME
# ============================================================
#
# Native Streamlit theme helpers.
#
# No HTML.
# No CSS injection.
# No unsafe_allow_html.
# ============================================================


DARK_THEME = {
    "background": "#050509",
    "secondary_background": "#0B0B14",
    "text": "#F8FAFC",
    "primary": "#8B5CF6",
    "accent": "#3B82F6",
    "cyan": "#22D3EE",
    "pink": "#EC4899",
}


LIGHT_THEME = {
    "background": "#F7F9FF",
    "secondary_background": "#EEF3FF",
    "text": "#111936",
    "primary": "#7C3AED",
    "accent": "#2563EB",
    "cyan": "#0891B2",
    "pink": "#DB2777",
}


def get_theme(theme: str = "dark") -> dict:
    """
    Return the CareerCopilot design tokens
    for the requested theme.
    """

    if theme == "light":

        return LIGHT_THEME.copy()

    return DARK_THEME.copy()


def load_theme() -> dict:
    """
    Compatibility helper used by app.py.

    Returns the default CareerCopilot theme tokens.
    """

    return get_theme("dark")