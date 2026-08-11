import streamlit as st
from app.storage.profile_manager import load_profile


def show():

    profile = load_profile()

    ats = profile.get("ats_score", 0)
    skills = len(profile.get("skills", []))
    health = profile.get("career_health", 0)
    resume = profile.get("resume_name", "")

    st.markdown("### 📊 Career Metrics")

    st.caption(
        "A quick snapshot of your current career readiness."
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

        with st.container(
            border=True,
            key="metric-ats",
        ):

            st.markdown("### 🎯")

            st.metric(
                "ATS Score",
                f"{ats}%",
                delta="+8",
            )

            st.caption(
                "Resume compatibility"
            )

    # ========================================================
    # SKILLS
    # ========================================================

    with col2:

        with st.container(
            border=True,
            key="metric-skills",
        ):

            st.markdown("### 🧠")

            st.metric(
                "Skills",
                skills,
                delta="+2",
            )

            st.caption(
                "Skills identified"
            )

    # ========================================================
    # CAREER HEALTH
    # ========================================================

    with col3:

        with st.container(
            border=True,
            key="metric-health",
        ):

            st.markdown("### 💚")

            st.metric(
                "Career Health",
                f"{health}%",
                delta="+5",
            )

            st.caption(
                "Overall readiness"
            )

    # ========================================================
    # RESUME
    # ========================================================

    with col4:

        with st.container(
            border=True,
            key="metric-resume",
        ):

            st.markdown("### 📄")

            status = (
                "Uploaded ✅"
                if resume
                else "Not Uploaded"
            )

            st.metric(
                "Resume",
                status,
            )

            st.caption(
                "Profile status"
            )