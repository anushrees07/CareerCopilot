import streamlit as st


def initialize_theme():

    if "theme" not in st.session_state:
        st.session_state.theme = "dark"


def toggle_theme():

    st.session_state.theme = (
        "light"
        if st.session_state.theme == "dark"
        else "dark"
    )


def current_theme():

    return st.session_state.theme