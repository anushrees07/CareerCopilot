from __future__ import annotations

import streamlit as st

from app.core.navigation import (
    RESUME_ANALYZER,
    OPPORTUNITIES,
    AI_COACH,
    ROADMAP,
    navigate,
)


def show() -> None:
    """Render CareerCopilot quick actions."""

    st.markdown("## ⚡ Quick Actions")

    st.caption(
        "Jump directly into the actions that move your career forward."
    )

    actions = [
        (
            "📄",
            "Analyze Resume",
            "Improve ATS compatibility and understand your resume.",
            RESUME_ANALYZER,
        ),
        (
            "💼",
            "Find Opportunities",
            "Discover internships that match your profile.",
            OPPORTUNITIES,
        ),
        (
            "🤖",
            "Ask AI Coach",
            "Get personalized career guidance from your AI coach.",
            AI_COACH,
        ),
        (
            "🗺️",
            "Build Roadmap",
            "Create a focused plan for your next career milestone.",
            ROADMAP,
        ),
    ]

    columns = st.columns(
        4,
        gap="medium",
    )

    for column, (icon, title, description, page) in zip(
        columns,
        actions,
    ):

        with column:

            with st.container(
                border=True,
            ):

                st.markdown(
                    f"### {icon}"
                )

                st.markdown(
                    f"**{title}**"
                )

                st.caption(
                    description
                )

                st.write("")

                if st.button(
                    "Open →",
                    key=f"quick_action_{page}",
                    use_container_width=True,
                ):

                    navigate(page)
                    st.rerun()