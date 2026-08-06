import streamlit as st


def show(
    title,
    subtitle="",
):

    st.markdown(f"## {title}")

    if subtitle:
        st.caption(subtitle)