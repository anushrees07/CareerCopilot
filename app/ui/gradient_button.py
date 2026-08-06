import streamlit as st


def show(
    label: str,
    key: str,
    icon: str = "✨",
    disabled: bool = False,
):

    return st.button(
        f"{icon}  {label}",
        key=key,
        use_container_width=True,
        disabled=disabled,
        type="primary",
    )