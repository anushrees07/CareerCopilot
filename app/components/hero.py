
from __future__ import annotations

import streamlit as st

from app.core.navigation import navigate


def show() -> None:
    left, right = st.columns(
        [1.7, 1],
        gap="large",
    )

    # --------------------------------------------------------
    # HERO CONTENT
    # --------------------------------------------------------

    with left:
        st.caption("✦ YOUR AI-POWERED CAREER WORKSPACE")

        st.title("Build Your Dream Career.")

        st.subheader(
            "Make your next career move with clarity."
        )

        st.write(
            "Understand your strengths, improve your resume, "
            "discover relevant internships, and prepare for "
            "the opportunities ahead."
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

        st.caption(
            "Start with your resume or explore opportunities. "
            "Your next step is yours to choose."
        )

    # --------------------------------------------------------
    # CAREER SNAPSHOT
    # --------------------------------------------------------

    with right:
        with st.container(border=True):
            st.markdown("### 🚀 Career Snapshot")

            st.caption(
                "The tools that bring your career journey together."
            )

            st.divider()

            features = [
                (
                    "📄",
                    "Resume Intelligence",
                    "Analyze your resume and identify areas to improve.",
                ),
                (
                    "🤖",
                    "Multiple AI Providers",
                    "Work with the supported AI provider integrations.",
                ),
                (
                    "📈",
                    "ATS Insights",
                    "Understand how your resume aligns with job requirements.",
                ),
                (
                    "💼",
                    "Internship Discovery",
                    "Explore opportunities relevant to your career goals.",
                ),
                (
                    "🗺️",
                    "Career Roadmaps",
                    "Get direction on the skills and steps ahead.",
                ),
            ]

            for index, (icon, title, description) in enumerate(features):
                st.markdown(f"**{icon}  {title}**")
                st.caption(description)

                if index != len(features) - 1:
                    st.divider()
