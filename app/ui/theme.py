from pathlib import Path
import streamlit as st


def load_theme():

    css = Path("assets/styles.css")

    if css.exists():

        st.markdown(
            f"<style>{css.read_text(encoding='utf-8')}</style>",
            unsafe_allow_html=True,
        )