from __future__ import annotations

import streamlit as st

from app.storage.profile_manager import load_profile


# ============================================================
# CAREER METRICS
# ============================================================


def show() -> None:

    profile = load_profile()

    ats_score = profile.get(
        "ats_score",
        0,
    )

    skills = len(
        profile.get(
            "skills",
            [],
        )
    )

    career_health = profile.get(
        "career_health",
        0,
    )

    resume_name = profile.get(
        "resume_name",
        "",
    )

    st.markdown(
        "## 📊 Career Metrics"
    )

    st.caption(
        "A live snapshot of your current career readiness."
    )

    st.write("")

    col1, col2, col3, col4 = st.columns(
        4,
        gap="medium",
    )

    # ========================================================
    # ATS
    # ========================================================

    with col1:

        with st.container(border=True):

            st.markdown("### 🎯")

            st.metric(
                "ATS Score",
                f"{ats_score}%",
            )

            st.caption(
                "Resume compatibility"
            )

    # ========================================================
    # SKILLS
    # ========================================================

    with col2:

        with st.container(border=True):

            st.markdown("### 🧠")

            st.metric(
                "Skills",
                skills,
            )

            st.caption(
                "Skills identified"
            )

    # ========================================================
    # CAREER HEALTH
    # ========================================================

    with col3:

        with st.container(border=True):

            st.markdown("### 💜")

            st.metric(
                "Career Health",
                f"{career_health}%",
            )

            st.caption(
                "Overall readiness"
            )

    # ========================================================
    # RESUME
    # ========================================================

    with col4:

        with st.container(border=True):

            st.markdown("### 📄")

            if resume_name:

                st.metric(
                    "Resume",
                    "Ready",
                )

                st.caption(
                    "Resume uploaded"
                )

            else:

                st.metric(
                    "Resume",
                    "Missing",
                )

                st.caption(
                    "Upload your resume"
                )