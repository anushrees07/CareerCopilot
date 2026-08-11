from pathlib import Path
import streamlit as st


def load_theme():
    """
    Loads the CareerCopilot visual system.

    Dark mode is the default.
    Light mode uses the same components and layout,
    but switches the CSS variables.
    """

    css_path = Path("assets/css/styles.css")

    if not css_path.exists():
        st.error(f"CareerCopilot CSS not found: {css_path}")
        return

    css = css_path.read_text(encoding="utf-8")

    theme = st.session_state.get("theme", "dark")

    if theme == "light":
        theme_css = """
        html {
            color-scheme: light;
        }

        body {
            background: #f6f7fb !important;
        }
        """
    else:
        theme_css = """
        html {
            color-scheme: dark;
        }

        body {
            background: #060816 !important;
        }
        """

    st.markdown(
        f"""
        <style>
        {theme_css}

        {css}
        </style>
        """,
        unsafe_allow_html=True,
    )