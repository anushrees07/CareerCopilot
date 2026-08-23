import streamlit as st

from app.core.navigation import (
    RESUME_ANALYZER,
    OPPORTUNITIES,
    AI_COACH,
    ROADMAP,
    navigate,
)


def show():
    """Render CareerCopilot quick actions."""

    st.markdown("### Quick Actions")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "📄 Analyze Resume",
            use_container_width=True,
            key="quick_resume",
        ):
            navigate(RESUME_ANALYZER)
            st.rerun()

        if st.button(
            "💼 Find Opportunities",
            use_container_width=True,
            key="quick_opportunities",
        ):
            navigate(OPPORTUNITIES)
            st.rerun()

    with col2:

        if st.button(
            "🤖 Ask AI Coach",
            use_container_width=True,
            key="quick_ai_coach",
        ):
            navigate(AI_COACH)
            st.rerun()

        if st.button(
            "🗺️ Build Roadmap",
            use_container_width=True,
            key="quick_roadmap",
        ):
            navigate(ROADMAP)
            st.rerun()