
from __future__ import annotations

import streamlit as st

from app.storage.profile_manager import load_profile


def _format_score(value: object) -> str:
    """Return a safe, readable ATS score."""
    if value is None or value == "":
        return "Not calculated"

    try:
        score = float(value)
    except (TypeError, ValueError):
        return "Not available"

    if not 0 <= score <= 100:
        return "Not available"

    return f"{score:g}%"


def _get_skills(value: object) -> list[str]:
    """Normalize skills into a clean list of strings."""
    if not isinstance(value, (list, tuple, set)):
        return []

    return [
        str(skill).strip()
        for skill in value
        if skill is not None and str(skill).strip()
    ]


def show() -> None:
    """Render the user's career profile."""

    profile = load_profile() or {}

    resume_name = profile.get("resume_name")
    has_resume = isinstance(resume_name, str) and bool(
        resume_name.strip()
    )

    st.markdown("## 👤 Career Profile")

    st.caption(
        "Your career information and AI-generated insights "
        "based on your resume."
    )

    # --------------------------------------------------------
    # EMPTY STATE
    # --------------------------------------------------------

    if not has_resume:
        with st.container(border=True):
            st.markdown("### 📄 Your Career Profile is Waiting")

            st.write(
                "Upload your resume to build your career profile "
                "and access personalized resume insights."
            )

            st.write("")

            col1, col2, col3 = st.columns(3, gap="medium")

            with col1:
                st.markdown("### 📊")
                st.caption("ATS Insights")

            with col2:
                st.markdown("### 🧠")
                st.caption("Skill Intelligence")

            with col3:
                st.markdown("### 🤖")
                st.caption("AI Career Summary")

        return

    # --------------------------------------------------------
    # RESUME OVERVIEW
    # --------------------------------------------------------

    with st.container(border=True):
        left, right = st.columns(
            [1.5, 1],
            gap="large",
        )

        with left:
            st.markdown("### 📄 Uploaded Resume")

            st.success(resume_name.strip())

            st.caption("Resume available in your career profile")

        with right:
            st.markdown("### 🎯 ATS Score")

            st.metric(
                label="Resume compatibility",
                value=_format_score(profile.get("ats_score")),
            )

    st.write("")

    # --------------------------------------------------------
    # EXTRACTED SKILLS
    # --------------------------------------------------------

    skills = _get_skills(profile.get("skills", []))

    with st.container(border=True):
        st.markdown("### 🧠 Extracted Skills")

        st.caption(
            "Skills identified and stored in your career profile."
        )

        if skills:
            skill_columns = st.columns(3, gap="small")

            for index, skill in enumerate(skills):
                with skill_columns[index % 3]:
                    st.success(skill)

            st.caption(f"{len(skills)} skills identified")

        else:
            st.info(
                "No extracted skills are available yet. "
                "Try analyzing your resume again."
            )

    st.write("")

    # --------------------------------------------------------
    # AI CAREER SUMMARY
    # --------------------------------------------------------

    with st.container(border=True):
        st.markdown("### 🤖 AI Career Summary")

        feedback = profile.get("ai_feedback", "")

        if isinstance(feedback, str) and feedback.strip():
            st.write(feedback.strip())
        else:
            st.info(
                "Your AI career summary will appear here after "
                "your resume has been analyzed."
            )
