import streamlit as st

from app.storage.profile_manager import load_profile

from app.core.navigation import (
    DASHBOARD,
    RESUME_ANALYZER,
    OPPORTUNITIES,
    AI_COACH,
    INTERVIEW_PREP,
    ROADMAP,
    ANALYTICS,
    SETTINGS,
    get_current_page,
    navigate,
)


# ============================================================
# CAREERCOPILOT SIDEBAR
# ============================================================


def nav_button(label, page, icon):
    """
    Reusable CareerCopilot navigation button.

    Navigation uses stable internal page IDs instead of
    UI labels.
    """

    current_page = get_current_page()

    is_active = (
        current_page == page
    )

    button_label = (
        f"●  {icon}  {label}"
        if is_active
        else f"{icon}  {label}"
    )

    if st.button(
        button_label,
        use_container_width=True,
        key=f"sidebar_nav_{page}",
        type=(
            "primary"
            if is_active
            else "secondary"
        ),
    ):

        navigate(page)

        st.rerun()


# ============================================================
# SIDEBAR
# ============================================================


def show():
    """
    Premium CareerCopilot sidebar.

    Preserves the existing profile, ATS, skills,
    navigation, and Career Health functionality.
    """

    profile = load_profile()

    # ========================================================
    # BRAND
    # ========================================================

    st.markdown(
        "# 🚀 CareerCopilot"
    )

    st.caption(
        "Build Your Dream Career"
    )

    st.divider()

    # ========================================================
    # PROFILE
    # ========================================================

    st.markdown(
        "### 👤 Profile"
    )

    resume_name = profile.get(
        "resume_name",
        "",
    )

    ats_score = profile.get(
        "ats_score",
        0,
    )

    skills = profile.get(
        "skills",
        [],
    )

    if resume_name:

        st.success(
            "Resume Uploaded"
        )

        st.caption(
            resume_name
        )

    else:

        st.warning(
            "No Resume"
        )

    profile_col1, profile_col2 = st.columns(2)

    with profile_col1:

        st.metric(
            "ATS",
            f"{ats_score}%",
        )

    with profile_col2:

        st.metric(
            "Skills",
            len(skills),
        )

    st.divider()

    # ========================================================
    # NAVIGATION
    # ========================================================

    nav_button(
        "Dashboard",
        DASHBOARD,
        "🏠",
    )

    nav_button(
        "Resume Intelligence",
        RESUME_ANALYZER,
        "📄",
    )

    nav_button(
        "Opportunities",
        OPPORTUNITIES,
        "💼",
    )

    nav_button(
        "AI Coach",
        AI_COACH,
        "🤖",
    )

    nav_button(
        "Interview Prep",
        INTERVIEW_PREP,
        "🎤",
    )

    nav_button(
        "Roadmap",
        ROADMAP,
        "🗺️",
    )

    nav_button(
        "Analytics",
        ANALYTICS,
        "📊",
    )

    nav_button(
        "Settings",
        SETTINGS,
        "⚙️",
    )

    st.divider()

    # ========================================================
    # CAREER HEALTH
    # ========================================================

    st.markdown(
        "💚 Career Health"
    )

    career_health = profile.get(
        "career_health",
        0,
    )

    try:

        career_health = float(
            career_health
        )

    except (
        TypeError,
        ValueError,
    ):

        career_health = 0.0

    career_health = max(
        0.0,
        min(
            career_health,
            100.0,
        ),
    )

    st.progress(
        career_health / 100
    )

    st.caption(
        f"{career_health:.0f}% overall readiness"
    )

    st.divider()

    st.caption(
        "✨ Powered by AI"
    )