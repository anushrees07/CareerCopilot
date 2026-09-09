from __future__ import annotations

import streamlit as st

from app.core.navigation import navigate


# ============================================================
# CAREERCOPILOT HERO
# NATIVE STREAMLIT VERSION
# ZERO HTML
# ============================================================


def show() -> None:

    left, right = st.columns(
        [1.7, 1],
        gap="large",
    )

    # ========================================================
    # LEFT
    # ========================================================

    with left:

        st.caption(
            "✦ AI-POWERED CAREER PLATFORM"
        )

        st.markdown(
            "# Build Your Dream"
        )

        st.markdown(
            "# Career With AI"
        )

        st.write(
            """
            Analyze your resume, discover internships,
            identify skill gaps, prepare for interviews,
            generate career roadmaps, and accelerate
            your career with AI.
            """
        )

        st.write("")

        action_1, action_2 = st.columns(
            2,
            gap="small",
        )

        with action_1:

            if st.button(
                "📄 Analyze Resume",
                key="hero_analyze_resume",
                use_container_width=True,
                type="primary",
            ):
                navigate("resume_analyzer")
                st.rerun()

        with action_2:

            if st.button(
                "💼 Explore Opportunities",
                key="hero_opportunities",
                use_container_width=True,
                type="primary",
            ):
                navigate("opportunities")
                st.rerun()

    # ========================================================
    # RIGHT
    # ========================================================

    with right:

        with st.container(border=True):

            st.markdown(
                "## 🚀 Career Snapshot"
            )

            st.caption(
                "Your AI-powered career command center."
            )

            st.divider()

            features = [
                ("📄", "Resume Intelligence"),
                ("🤖", "Multi-AI Providers"),
                ("📈", "ATS Optimization"),
                ("💼", "Opportunity Matching"),
                ("🗺️", "Personalized Roadmap"),
            ]

            for icon, title in features:

                st.markdown(
                    f"**{icon}  {title}**"
                )

                st.caption(
                    "Ready to use"
                )