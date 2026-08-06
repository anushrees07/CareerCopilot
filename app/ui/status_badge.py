import streamlit as st


def show(
    text,
    color="green",
):

    colors = {

        "green": "🟢",

        "blue": "🔵",

        "yellow": "🟡",

        "red": "🔴",

        "purple": "🟣",

    }

    st.caption(
        f"{colors.get(color,'⚪')} {text}"
    )