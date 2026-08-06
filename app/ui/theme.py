from pathlib import Path
import streamlit as st


def load_theme():
    css_path = Path("assets/css/styles.css")

    if css_path.exists():
        with open(css_path, "r", encoding="utf-8") as css_file:
            st.markdown(
                f"<style>{css_file.read()}</style>",
                unsafe_allow_html=True,
            )
    else:
        st.warning(f"CSS file not found: {css_path}")