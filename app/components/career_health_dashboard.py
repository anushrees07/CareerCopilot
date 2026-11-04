
from __future__ import annotations

import streamlit as st

from app.storage.profile_manager import load_profile


def _safe_score(value: object) -> int | None:
    """Validate a score without silently converting invalid data to zero."""
    if value is None or value == "":
        return None

    try:
        score = float(value)
    except (TypeError, ValueError):
        return None

    if not 0 <= score <= 100:
        return None

    return round(score)


def _get_skills(value: object) -> list:
    """Return a safe list of extracted skills."""
    if not isinstance(value, (list, tuple, set)):
        return []

    return [
        skill
        for skill in value
        if skill is not None and str(skill).strip()
    ]


def _progress_row(
    label: str,
    value: int | None,
    icon: str,
) -> None:
    """Display a progress indicator or an unavailable state."""

    st.markdown(f"**{icon} {label}**")

    if value is None:
        st.caption("Not available yet")
        return

    st.progress(value / 100)
    st.caption(f"{value}%")


def show() -> None:
    """Render the profile-based Career Health estimate."""

    profile = load_profile() or {}

    if not isinstance(profile, dict):
        profile = {}

    resume_name = profile.get("resume_name", "")

    has_resume = (
        isinstance(resume_name, str)
        and bool(resume_name.strip())
    )

    st.markdown("## 💚 Career Health")

    st.caption(
        "A profile-based estimate using your resume and extracted skills. "
        "It is not a complete measure of internship readiness."
    )

    # --------------------------------------------------------
    # EMPTY STATE
    # --------------------------------------------------------

    if not has_resume:
        with st.container(border=True):
            st.markdown("### 🌱 Let's build your career profile")

            st.write(
                "Upload and analyze your resume to see your "
                "initial ATS and skill-based indicators here."
            )

            st.info(
                "Your Career Health score will appear after "
                "your first resume analysis."
            )

        return

    # --------------------------------------------------------
    # AVAILABLE PROFILE DATA
    # --------------------------------------------------------

    ats_score = _safe_score(profile.get("ats_score"))

    skills = _get_skills(profile.get("skills", []))

    skill_score = min(len(skills) * 10, 100)

    if ats_score is not None:
        internship_score = round(
            (ats_score + skill_score) / 2
        )

        career_score = round(
            (ats_score + skill_score + internship_score) / 3
        )
    else:
        internship_score = None
        career_score = None

    # --------------------------------------------------------
    # OVERALL SCORE
    # --------------------------------------------------------

    with st.container(border=True):
        st.markdown("### Overall Career Health")

        if career_score is None:
            st.metric(
                "Career Health Estimate",
                "Not available",
            )

            st.info(
                "Your ATS score could not be read. "
                "Please analyze your resume again."
            )

        else:
            st.metric(
                "Career Health Estimate",
                f"{career_score} / 100",
            )

            st.progress(career_score / 100)

            st.caption(
                "Calculated from the available ATS, skill and "
                "internship indicators."
            )

        st.divider()

        # ----------------------------------------------------
        # INDIVIDUAL INDICATORS
        # ----------------------------------------------------

        _progress_row(
            "Resume Strength",
            ats_score,
            "📄",
        )

        _progress_row(
            "Skill Readiness",
            skill_score,
            "🧠",
        )

        _progress_row(
            "Internship Readiness",
            internship_score,
            "💼",
        )

        st.markdown("**🤖 AI Readiness**")
        st.caption(
            "Not assessed yet. No AI-readiness evaluation "
            "is currently implemented."
        )

    # --------------------------------------------------------
    # NEXT STEP
    # --------------------------------------------------------

    if career_score is None:
        st.warning(
            "Re-analyze your resume to generate your career indicators."
        )

    elif career_score >= 80:
        st.success(
            "Your current profile indicators are looking strong. "
            "Focus next on projects, applications and interview practice."
        )

    elif career_score >= 60:
        st.info(
            "Your profile is developing. Strengthen your skills, "
            "resume evidence and practical projects."
        )

    else:
        st.warning(
            "Your profile needs more development. Start by improving "
            "your resume and building demonstrable technical skills."
        )
