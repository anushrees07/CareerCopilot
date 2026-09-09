from __future__ import annotations

import streamlit as st

from app.components.hero import show as show_hero
from app.components.stat_cards import show as show_stats
from app.components.profile_summary import show as show_profile
from app.components.career_health_dashboard import show as show_career_health
from app.components.quick_actions import show as show_quick_actions


# ============================================================
# CAREERCOPILOT DASHBOARD
# ============================================================
#
# Main career command center.
#
# ZERO HTML
# ZERO unsafe_allow_html
# Native Streamlit only.
# ============================================================


def show() -> None:

    show_hero()

    st.divider()

    show_stats()

    st.divider()

    show_daily_briefing()

    st.divider()

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
    
    # ========================================================
    # CAREER HEALTH + PROFILE
    # ========================================================

    health_col, profile_col = st.columns(
        [1, 1],
        gap="large",
    )

    with health_col:
        show_career_health()

    with profile_col:
        show_profile_snapshot()

    st.divider()

    # ========================================================
    # QUICK ACTIONS
    # ========================================================

    show_quick_actions()

    st.divider()

    # ========================================================
    # AI ASSISTANT
    # ========================================================

    show_ai_assistant()


# ============================================================
# DAILY BRIEFING
# ============================================================

def show_daily_briefing() -> None:

    st.markdown("## ✨ Daily Briefing")

    st.caption(
        "Your most important career actions for today."
    )

    with st.container(border=True):

        col1, col2, col3 = st.columns(
            3,
            gap="medium",
        )

        with col1:

            st.markdown(
                "### 📄 Resume"
            )

            st.write(
                "Keep your resume optimized for the roles you're targeting."
            )

            st.caption(
                "Priority: High"
            )

        with col2:

            st.markdown(
                "### 💼 Opportunities"
            )

            st.write(
                "Review new internships that match your current skills."
            )

            st.caption(
                "Priority: High"
            )

        with col3:

            st.markdown(
                "### 🧠 Skills"
            )

            st.write(
                "Spend focused time improving one career-critical skill."
            )

            st.caption(
                "Priority: Medium"
            )


# ============================================================
# CAREER HEALTH
# ============================================================

def show_career_health() -> None:

    st.markdown("## 💜 Career Health")

    st.caption(
        "A quick view of your current career readiness."
    )

    with st.container(border=True):

        health_score = 72

        st.markdown(
            "### Overall Readiness"
        )

        st.metric(
            "Career Health Score",
            f"{health_score}/100",
        )

        st.progress(
            health_score / 100
        )

        st.caption(
            "Keep improving your skills, resume, projects and interview readiness."
        )


# ============================================================
# PROFILE SNAPSHOT
# ============================================================

def show_profile_snapshot() -> None:

    st.markdown("## 👤 Career Snapshot")

    st.caption(
        "The foundation CareerCopilot is building around you."
    )

    with st.container(border=True):

        col1, col2 = st.columns(
            2,
            gap="medium",
        )

        with col1:

            st.markdown(
                "### 🎓 Education"
            )

            st.write(
                "Information Science & Engineering"
            )

            st.caption(
                "B.E. Student"
            )

        with col2:

            st.markdown(
                "### 🚀 Target"
            )

            st.write(
                "Software Engineering"
            )

            st.caption(
                "Internship → Full-time"
            )

        st.divider()

        col3, col4 = st.columns(
            2,
            gap="medium",
        )

        with col3:

            st.markdown(
                "### 🐍 Core Skill"
            )

            st.write(
                "Python"
            )

        with col4:

            st.markdown(
                "### 🤖 Focus"
            )

            st.write(
                "AI / GenAI"
            )


# ============================================================
# QUICK ACTIONS
# ============================================================

def show_quick_actions() -> None:

    st.markdown("## ⚡ Quick Actions")

    st.caption(
        "Jump directly into the work that moves your career forward."
    )

    col1, col2, col3, col4 = st.columns(
        4,
        gap="medium",
    )

    with col1:

        with st.container(border=True):

            st.markdown(
                "### 📄"
            )

            st.markdown(
                "**Analyze Resume**"
            )

            st.caption(
                "Get ATS insights and improvement suggestions."
            )

            if st.button(
                "Open",
                key="dashboard_resume",
                use_container_width=True,
            ):

                st.session_state["page"] = "resume_analyzer"
                st.rerun()

    with col2:

        with st.container(border=True):

            st.markdown(
                "### 💼"
            )

            st.markdown(
                "**Find Internships**"
            )

            st.caption(
                "Discover opportunities matching your profile."
            )

            if st.button(
                "Open",
                key="dashboard_opportunities",
                use_container_width=True,
            ):

                st.session_state["page"] = "opportunities"
                st.rerun()

    with col3:

        with st.container(border=True):

            st.markdown(
                "### 🧩"
            )

            st.markdown(
                "**Find Skill Gaps**"
            )

            st.caption(
                "See what skills you need to become more competitive."
            )

            if st.button(
                "Open",
                key="dashboard_skill_gap",
                use_container_width=True,
            ):

                st.session_state["page"] = "skill_gap"
                st.rerun()

    with col4:

        with st.container(border=True):

            st.markdown(
                "### 🎤"
            )

            st.markdown(
                "**Practice Interview**"
            )

            st.caption(
                "Prepare for technical and behavioral interviews."
            )

            if st.button(
                "Open",
                key="dashboard_interview",
                use_container_width=True,
            ):

                st.session_state["page"] = "interview_prep"
                st.rerun()


# ============================================================
# AI ASSISTANT
# ============================================================

def show_ai_assistant() -> None:

    st.markdown("## 🤖 AI Career Assistant")

    st.caption(
        "Your career copilot is ready to help."
    )

    with st.container(border=True):

        st.markdown(
            "### What should we work on?"
        )

        st.write(
            "Ask CareerCopilot about your resume, skills, internships, interviews or roadmap."
        )

        prompt = st.text_input(
            "Career question",
            placeholder="e.g. How can I improve my internship chances?",
            label_visibility="collapsed",
        )

        if st.button(
            "Ask CareerCopilot",
            key="dashboard_ai_assistant",
            use_container_width=True,
            type="primary",
        ):

            if not prompt.strip():

                st.warning(
                    "Enter a question first."
                )

            else:

                st.info(
                    "AI Assistant integration will connect to your configured AI provider here."
                )