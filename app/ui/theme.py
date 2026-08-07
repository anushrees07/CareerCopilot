from pathlib import Path
import streamlit as st


def load_theme():

    css_path = Path("assets/css/styles.css")

    if not css_path.exists():
        st.warning(
            f"CSS file not found: {css_path}"
        )
        return

    css = css_path.read_text(
        encoding="utf-8"
    )

    st.markdown(
        f"<style>{css}</style>",
        unsafe_allow_html=True,
    )