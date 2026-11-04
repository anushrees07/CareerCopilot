
from __future__ import annotations

import streamlit as st

from app.storage.profile_manager import load_profile


def _format_score(value: object) -> str:
    """Format a stored score without presenting missing data as zero."""
    if value is None or value == "":
        return "Not calculated"

    try:
        score = float(value)
    except (TypeError, ValueError):
        return "Not available"

    if not 0 <= score <= 100:
        return "Not available"

    return f"{score:g}%"


def _count_skills(value: object) -> int:
    """Safely count the skills stored in the profile."""
    if isinstance(value, (list, tuple, set)):
        return len(value)

    return 0


def show() -> None:
    profile = load_profile() or {}

    ats_score = _format_score(profile.get("ats_score"))
    career_health = _format_score(
        profile.get("career_health")
    )

    skills = _count_skills(profile.get("skills", []))

    resume_name = profile.get("resume_name")
    has_resume = isinstance(resume_name, str) and bool(
        resume_name.strip()
    )

    st.markdown("## 📊 Career Metrics")

    st.caption(
        "A snapshot of your current career profile and readiness."
    )

    st.write("")

    metrics = st.columns(4, gap="medium")

    # ATS SCORE
    with metrics[0]:
        with st.container(border=True):
            st.markdown("### 🎯")
            st.metric(
                label="ATS Score",
                value=ats_score,
            )
            st.caption("Resume compatibility")

    # SKILLS
    with metrics[1]:
        with st.container(border=True):
            st.markdown("### 🧠")
            st.metric(
                label="Skills",
                value=skills,
            )
            st.caption("Skills identified in your profile")

    # CAREER HEALTH
    with metrics[2]:
        with st.container(border=True):
            st.markdown("### 💜")
            st.metric(
                label="Career Health",
                value=career_health,
            )
            st.caption("Overall readiness")

    # RESUME STATUS
    with metrics[3]:
        with st.container(border=True):
            st.markdown("### 📄")

            st.metric(
                label="Resume",
                value="Ready" if has_resume else "Missing",
            )

            st.caption(
                "Resume uploaded"
                if has_resume
                else "Upload your resume to get started"
            )
