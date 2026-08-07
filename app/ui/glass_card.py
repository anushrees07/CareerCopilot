import streamlit as st


def show(
    title: str,
    value: str = "",
    subtitle: str = "",
    icon: str = "",
):

    with st.container(border=True):

        top_left, top_right = st.columns([5, 1])

        with top_left:
            st.markdown(f"### {icon} {title}")

        with top_right:
            st.markdown("✨")

        if value:
            st.markdown(f"## {value}")

        if subtitle:
            st.caption(subtitle)