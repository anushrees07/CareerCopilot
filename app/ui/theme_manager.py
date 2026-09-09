import streamlit as st


def initialize_theme() -> None:

    if "appearance" not in st.session_state:
        st.session_state.appearance = "dark"


def toggle_theme() -> None:

    current = st.session_state.get(
        "appearance",
        "dark",
    )

    st.session_state.appearance = (
        "light"
        if current == "dark"
        else "dark"
    )


def current_theme() -> str:

    return st.session_state.get(
        "appearance",
        "dark",
    )