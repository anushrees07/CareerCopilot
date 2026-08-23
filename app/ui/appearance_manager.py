import streamlit as st


# ============================================================
# CAREERCOPILOT APPEARANCE MANAGER
# ============================================================
#
# Dark is the DEFAULT.
# Light is completely controlled through CSS variables.
#
# This avoids the old problem where dark CSS remained active
# after switching to light mode.
# ============================================================


def initialize():
    """
    Initialize CareerCopilot appearance.

    Dark mode is always the first-launch default.
    """

    if "appearance" not in st.session_state:
        st.session_state.appearance = "dark"


def get_current_theme():
    """
    Return current theme.
    """

    return st.session_state.get(
        "appearance",
        "dark",
    )


def set_theme(theme: str):
    """
    Change theme safely.
    """

    if theme not in ("dark", "light"):
        theme = "dark"

    st.session_state.appearance = theme


# ============================================================
# THEME VARIABLES
# ============================================================

DARK_THEME = """
:root {
    color-scheme: dark;

    --cc-bg: #030712;
    --cc-bg-secondary: #071225;

    --cc-text: #f8fafc;
    --cc-text-soft: #d6deec;
    --cc-text-muted: #8c9ab0;

    --cc-card: rgba(10, 20, 43, 0.58);
    --cc-card-strong: rgba(12, 24, 51, 0.78);

    --cc-border: rgba(105, 190, 255, 0.22);
    --cc-border-strong: rgba(110, 231, 255, 0.42);

    --cc-purple: #8b5cf6;
    --cc-purple-bright: #a855f7;

    --cc-blue: #3b82f6;
    --cc-cyan: #22d3ee;
    --cc-pink: #ec4899;

    --cc-shadow:
        0 25px 70px rgba(0, 0, 0, 0.45),
        0 0 35px rgba(59, 130, 246, 0.08);

    --cc-button-text: #ffffff;

    --cc-sidebar:
        linear-gradient(
            180deg,
            rgba(3, 9, 24, 0.96),
            rgba(7, 14, 32, 0.92)
        );

    --cc-divider:
        rgba(148, 163, 184, 0.14);
}
"""


LIGHT_THEME = """
:root {
    color-scheme: light;

    --cc-bg: #f7f9ff;
    --cc-bg-secondary: #eef3ff;

    --cc-text: #111936;
    --cc-text-soft: #334155;
    --cc-text-muted: #64748b;

    --cc-card: rgba(255, 255, 255, 0.62);
    --cc-card-strong: rgba(255, 255, 255, 0.82);

    --cc-border: rgba(99, 102, 241, 0.16);
    --cc-border-strong: rgba(99, 102, 241, 0.30);

    --cc-purple: #7c3aed;
    --cc-purple-bright: #8b5cf6;

    --cc-blue: #2563eb;
    --cc-cyan: #0891b2;
    --cc-pink: #db2777;

    --cc-shadow:
        0 22px 55px rgba(79, 70, 229, 0.10),
        0 8px 25px rgba(15, 23, 42, 0.06);

    --cc-button-text: #ffffff;

    --cc-sidebar:
        linear-gradient(
            180deg,
            rgba(255, 255, 255, 0.92),
            rgba(242, 246, 255, 0.94)
        );

    --cc-divider:
        rgba(100, 116, 139, 0.16);
}
"""


# ============================================================
# APPLY THEME
# ============================================================

def apply_theme():
    """
    Inject only the currently selected theme variables.
    """

    theme = get_current_theme()

    if theme == "light":
        css = LIGHT_THEME
    else:
        css = DARK_THEME

    st.markdown(
        f"""
        <style>
        {css}
        </style>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# THEME SWITCHER
# ============================================================

def show_theme_switcher():
    """
    Premium Dark / Light theme selector.
    """

    current = get_current_theme()

    st.markdown(
        '<div class="cc-theme-label">Appearance</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(
        2,
        gap="small",
    )

    with col1:

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

            set_theme("dark")
            st.rerun()

    with col2:

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

            set_theme("light")
            st.rerun()