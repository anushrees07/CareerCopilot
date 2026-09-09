from __future__ import annotations

import streamlit as st


# ============================================================
# CAREERCOPILOT APPEARANCE MANAGER
# ============================================================
#
# ZERO HTML
# ZERO unsafe_allow_html
#
# Streamlit's native theme is controlled through
# .streamlit/config.toml.
#
# This module handles the user's appearance preference
# and the UI controls around it.
# ============================================================


SUPPORTED_THEMES = (
    "dark",
    "light",
)


DEFAULT_THEME = "dark"


# ============================================================
# INITIALIZATION
# ============================================================

def initialize() -> None:
    """
    Initialize the CareerCopilot appearance state.

    Dark mode is the default.
    """

    if "appearance" not in st.session_state:

        st.session_state.appearance = DEFAULT_THEME


# ============================================================
# GET CURRENT THEME
# ============================================================

def get_current_theme() -> str:
    """
    Return the currently selected appearance.
    """

    return st.session_state.get(
        "appearance",
        DEFAULT_THEME,
    )


# ============================================================
# SET THEME
# ============================================================

def set_theme(theme: str) -> None:
    """
    Safely update the appearance preference.
    """

    if theme not in SUPPORTED_THEMES:

        theme = DEFAULT_THEME

    st.session_state.appearance = theme


# ============================================================
# TOGGLE THEME
# ============================================================

def toggle_theme() -> None:
    """
    Toggle between dark and light mode.
    """

    current = get_current_theme()

    if current == "dark":

        set_theme("light")

    else:

        set_theme("dark")


# ============================================================
# APPLY THEME
# ============================================================

def apply_theme() -> None:
    """
    Compatibility function.

    The previous implementation injected CSS directly into
    the page using unsafe HTML.

    That is intentionally removed.

    Streamlit's native theme configuration now owns the
    global application appearance.
    """

    return None


# ============================================================
# THEME SWITCHER
# ============================================================

def show_theme_switcher() -> None:
    """
    Render the native Streamlit theme switcher.
    """

    current = get_current_theme()

    st.caption(
        "Appearance"
    )

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