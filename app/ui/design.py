from __future__ import annotations

import streamlit as st


# ============================================================
# CAREERCOPILOT NATIVE DESIGN SYSTEM
# ZERO HTML
# ============================================================


def section_header(
    eyebrow: str,
    title: str,
    description: str | None = None,
) -> None:
    """
    Premium section heading using native Streamlit components.
    """

    st.caption(eyebrow.upper())

    st.markdown(f"# {title}")

    if description:
        st.caption(description)


def divider() -> None:
    """Visual spacing divider."""
    st.divider()


def metric_card(
    icon: str,
    label: str,
    value: str | int | float,
    description: str = "",
) -> None:
    """
    Native Streamlit metric card.
    """

    with st.container(border=True):
        st.markdown(f"### {icon}")
        st.metric(
            label=label,
            value=value,
        )

        if description:
            st.caption(description)


def feature_card(
    icon: str,
    title: str,
    description: str,
) -> None:
    """
    Reusable feature card.
    """

    with st.container(border=True):
        st.markdown(f"### {icon}  {title}")
        st.caption(description)


def status_card(
    icon: str,
    title: str,
    status: str,
    description: str = "",
) -> None:
    """
    Status-style card.
    """

    with st.container(border=True):
        st.markdown(f"### {icon}  {title}")
        st.write(f"**{status}**")

        if description:
            st.caption(description)


def progress_card(
    title: str,
    value: float,
    description: str = "",
) -> None:
    """
    Progress visualization.
    """

    with st.container(border=True):
        st.markdown(f"### {title}")

        st.progress(
            max(0.0, min(1.0, value))
        )

        if description:
            st.caption(description)


def action_button(
    label: str,
    key: str,
) -> bool:
    """
    Consistent primary action button.
    """

    return st.button(
        label,
        key=key,
        use_container_width=True,
        type="primary",
    )