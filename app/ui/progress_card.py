import streamlit as st


def show(
    title,
    progress,
    subtitle="",
):

    with st.container(border=True):

        st.markdown(f"### {title}")

        st.progress(progress / 100)

        st.markdown(
            f"### {progress}%"
        )

        if subtitle:

            st.caption(subtitle)