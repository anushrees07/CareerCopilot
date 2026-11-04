
from __future__ import annotations

import streamlit as st

from app.components.hero import show as show_hero
from app.components.stat_cards import show as show_stats
from app.components.profile_summary import show as show_profile
from app.components.career_health_dashboard import (
    show as show_career_health,
)
from app.components.quick_actions import show as show_quick_actions


# ============================================================
# CAREERCOPILOT DASHBOARD
# ============================================================
# Main career command center.
#
# Uses existing native Streamlit components.
# Preserves existing navigation and component architecture.
# No unsafe_allow_html or custom HTML cards.
# ============================================================


def show() -> None:
    """Render the main CareerCopilot dashboard."""

    show_hero()

    st.divider()

    show_stats()

    st.divider()

    show_daily_briefing()

    st.divider()

    # Career health and profile snapshot
    health_col, profile_col = st.columns(
        [1, 1],
        gap="large",
    )

    with health_col:
        show_career_health()

    with profile_col:
        show_profile()

    st.divider()

    show_quick_actions()

    st.divider()

    show_ai_assistant()


# ============================================================
# DAILY BRIEFING
# ============================================================

def show_daily_briefing() -> None:
    st.markdown("## Daily Briefing")

    st.caption(
        "Your most important career actions for today."
    )

    with st.container(border=True):
        col1, col2, col3 = st.columns(
            3,
            gap="medium",
        )

        with col1:
            st.markdown("### Resume")
            st.write(
                "Keep your resume optimized for the roles "
                "you're targeting."
            )
            st.caption("Priority: High")

        with col2:
            st.markdown("### Opportunities")
            st.write(
                "Review internships that match your "
                "current skills and interests."
            )
            st.caption("Priority: High")

        with col3:
            st.markdown("### Skills")
            st.write(
                "Spend focused time improving one "
                "career-critical skill."
            )
            st.caption("Priority: Medium")


# ============================================================
# AI ASSISTANT
# ============================================================

def show_ai_assistant() -> None:
    st.markdown("## AI Career Assistant")

    st.caption(
        "Your career copilot is ready to help."
    )

    with st.container(border=True):
        st.markdown("### What should we work on?")

        st.write(
            "Ask CareerCopilot about your resume, skills, "
            "internships, interviews or career roadmap."
        )

        prompt = st.text_input(
            "Career question",
            placeholder=(
                "e.g. How can I improve my internship chances?"
            ),
            label_visibility="collapsed",
            key="dashboard_career_question",
        )

        if st.button(
            "Ask CareerCopilot",
            key="dashboard_ai_assistant",
            use_container_width=True,
            type="primary",
        ):
            if not prompt.strip():
                st.warning("Enter a question first.")
            else:
                st.info(
                    "Your question is ready. The AI provider "
                    "integration will be connected through "
                    "the existing assistant backend."
                )
