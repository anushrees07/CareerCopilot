import streamlit as st

from app.storage.profile_manager import load_profile


# ============================================================
# CAREERCOPILOT CAREER METRICS
# PREMIUM V2
# ============================================================


def show():
    """
    Career Metrics dashboard section.

    Data is sourced from the existing profile manager.
    No fake deltas or invented analytics are displayed.
    Visual styling is handled by the global UI/CSS system.
    """

    profile = load_profile()

    # ========================================================
    # REAL PROFILE DATA
    # ========================================================

    ats = profile.get("ats_score", 0)

    skills = len(
        profile.get("skills", [])
    )

    health = profile.get(
        "career_health",
        0,
    )

    resume = profile.get(
        "resume_name",
        "",
    )

    # ========================================================
    # SECTION HEADER
    # ========================================================

    st.markdown(
        "## 📊 Career Metrics"
    )

    st.caption(
        "A quick snapshot of your current career readiness."
    )

    st.write("")

    # ========================================================
    # METRIC GRID
    # ========================================================

    col1, col2, col3, col4 = st.columns(
        4,
        gap="medium",
    )

    # ========================================================
    # ATS SCORE
    # ========================================================

    with col1:

        with st.container(
            border=True,
            key="metric-ats",
        ):

            st.markdown(
                "🎯"
            )

            st.metric(
                label="ATS Score",
                value=f"{ats}%",
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

            st.markdown(
                "🧠"
            )

            st.metric(
                label="Skills",
                value=skills,
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

            st.markdown(
                "💚"
            )

            st.metric(
                label="Career Health",
                value=f"{health}%",
            )

            st.caption(
                "Overall readiness"
            )

    # ========================================================
    # RESUME STATUS
    # ========================================================

    with col4:

        with st.container(
            border=True,
            key="metric-resume",
        ):

            st.markdown(
                "📄"
            )

            if resume:

                status = "Ready"

                caption = "Resume uploaded"

            else:

                status = "Missing"

                caption = "Upload your resume"

            st.metric(
                label="Resume",
                value=status,
            )

            st.caption(
                caption
            )