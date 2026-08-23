from pathlib import Path
import streamlit as st


# ============================================================
# CAREERCOPILOT GLOBAL THEME LOADER
# ============================================================


def load_theme():

    base_dir = Path(__file__).resolve().parents[2]

    css_files = [
        base_dir / "assets" / "css" / "styles.css",
        base_dir / "assets" / "css" / "hero.css",
    ]

    css_parts = []

    for css_file in css_files:

        if not css_file.exists():
            continue

        try:
            css_parts.append(
                css_file.read_text(
                    encoding="utf-8"
                )
            )

        except Exception:
            continue

    if not css_parts:
        return

    css = "\n\n".join(css_parts)

    st.markdown(
        f"""
        <style>
        {css}
        </style>
        """,
        unsafe_allow_html=True,
    )