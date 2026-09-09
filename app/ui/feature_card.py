import streamlit as st


def show(
    title: str,
    description: str,
    icon: str = "✨",
    color: str = "#8B5CF6",
) -> None:

    with st.container(
        border=True,
        key=f"feature_{title}",
    ):

        st.subheader(
            f"{icon}  {title}"
        )

        st.write(
            description
        )

        st.caption(
            f"✦ {color}"
        )