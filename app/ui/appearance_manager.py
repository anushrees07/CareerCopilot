
from __future__ import annotations

import streamlit as st

from app.ui.theme import (
    DEFAULT_THEME,
    SUPPORTED_THEMES,
    get_theme,
)


# ============================================================
# CAREERCOPILOT APPEARANCE MANAGER
# ============================================================
#
# Native Streamlit appearance management.
#
# No HTML.
# No JavaScript.
# No unsafe_allow_html.
#
# Preserves existing public functions.
# ============================================================


# ============================================================
# INITIALIZATION
# ============================================================

def initialize() -> None:
    """
    Initialize the user's appearance preference.

    Dark mode remains the default.
    """

    if "appearance" not in st.session_state:
        st.session_state["appearance"] = DEFAULT_THEME

    if st.session_state["appearance"] not in SUPPORTED_THEMES:
        st.session_state["appearance"] = DEFAULT_THEME


# ============================================================
# GET CURRENT THEME
# ============================================================

def get_current_theme() -> str:
    """
    Return the currently selected appearance.
    """

    initialize()

    return st.session_state["appearance"]


# ============================================================
# GET ACTIVE THEME TOKENS
# ============================================================

def get_active_theme() -> dict:
    """
    Return the design tokens for the active appearance.
    """

    return get_theme(get_current_theme())


# ============================================================
# SET THEME
# ============================================================

def set_theme(theme: str) -> None:
    """
    Safely update the appearance preference.
    """

    selected_theme = (
        theme.lower().strip()
        if isinstance(theme, str)
        else DEFAULT_THEME
    )

    if selected_theme not in SUPPORTED_THEMES:
        selected_theme = DEFAULT_THEME

    st.session_state["appearance"] = selected_theme


# ============================================================
# TOGGLE THEME
# ============================================================

def toggle_theme() -> None:
    """
    Toggle between dark and light appearances.
    """

    current = get_current_theme()

    if current == "dark":
        set_theme("light")
    else:
        set_theme("dark")


# ============================================================
# APPLY THEME
# ============================================================

def apply_theme() -> dict:
    """
    Return the active theme tokens.

    Custom CSS injection is intentionally not used.

    Streamlit's native global theme is configured separately
    through .streamlit/config.toml.

    Components can consume these tokens to render their
    active appearance using native Streamlit functionality.
    """

    return get_active_theme()


# ============================================================
# THEME SWITCHER
# ============================================================

def show_theme_switcher() -> None:
    """
    Display the native Streamlit theme controls.
    """

    current = get_current_theme()

    st.caption("Choose your appearance")

    dark_col, light_col = st.columns(
        2,
        gap="small",
    )

    with dark_col:
        if st.button(
            "🌙 Dark",
            key="cc_theme_dark",
            use_container_width=True,
            type=(
                "primary"
                if current == "dark"
                else "secondary"
            ),
        ):
            if current != "dark":
                set_theme("dark")
                st.rerun()

    with light_col:
        if st.button(
            "☀️ Light",
            key="cc_theme_light",
            use_container_width=True,
            type=(
                "primary"
                if current == "light"
                else "secondary"
            ),
        ):
            if current != "light":
                set_theme("light")
                st.rerun()

    active_theme = get_active_theme()

    st.caption(
        f"Active appearance: {active_theme['name'].capitalize()}"
    )


# ============================================================
# DISPLAY HELPERS
# ============================================================

def is_dark_mode() -> bool:
    """
    Return True when dark mode is active.
    """

    return get_current_theme() == "dark"


def is_light_mode() -> bool:
    """
    Return True when light mode is active.
    """

    return get_current_theme() == "light"
