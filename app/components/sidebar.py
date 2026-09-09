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

from app.ui.appearance_manager import show_theme_switcher


def _nav_button(
    label: str,
    page: str,
    icon: str,
) -> None:

    active = get_current_page() == page

    prefix = "✦ " if active else ""

    if st.button(
        f"{prefix}{icon}  {label}",
        key=f"sidebar_nav_{page}",
        use_container_width=True,
        type="primary" if active else "secondary",
    ):
        navigate(page)
        st.rerun()


def show() -> None:

    profile = load_profile()

    st.title("🚀")

    st.subheader("CareerCopilot")

    st.caption(
        "Build your career with AI."
    )

    st.divider()

    show_theme_switcher()

    st.divider()

    _nav_button(
        "Dashboard",
        DASHBOARD,
        "⌂",
    )

    _nav_button(
        "Resume Intelligence",
        RESUME_ANALYZER,
        "▣",
    )

    _nav_button(
        "Opportunities",
        OPPORTUNITIES,
        "◈",
    )

    _nav_button(
        "AI Coach",
        AI_COACH,
        "✦",
    )

    _nav_button(
        "Interview Prep",
        INTERVIEW_PREP,
        "◎",
    )

    _nav_button(
        "Roadmap",
        ROADMAP,
        "◇",
    )

    _nav_button(
        "Analytics",
        ANALYTICS,
        "◫",
    )

    _nav_button(
        "Settings",
        SETTINGS,
        "⚙",
    )

    st.divider()

    ats = profile.get(
        "ats_score",
        0,
    )

    skills = len(
        profile.get(
            "skills",
            [],
        )
    )

    health = profile.get(
        "career_health",
        0,
    )

    st.subheader(
        "📌 Career Pulse"
    )

    pulse_left, pulse_right = st.columns(
        2,
        gap="small",
    )

    with pulse_left:
        st.metric(
            "ATS",
            f"{ats}%",
        )

    with pulse_right:
        st.metric(
            "Skills",
            skills,
        )

    readiness = max(
        0,
        min(
            float(health),
            100,
        ),
    )

    st.progress(
        readiness / 100
    )

    st.caption(
        f"{readiness:.0f}% overall readiness"
    )

    st.divider()

    st.caption(
        "✦ Multi-AI career intelligence"
    )