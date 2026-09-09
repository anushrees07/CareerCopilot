from __future__ import annotations

import streamlit as st

from app.storage.profile_manager import load_profile


def _progress_row(
    label: str,
    value: int,
    icon: str,
) -> None:

    value = max(
        0,
        min(
            100,
            int(value),
        ),
    )

    st.markdown(
        f"**{icon} {label}**"
    )

    st.progress(
        value / 100
    )

    st.caption(
        f"{value}%"
    )


def show() -> None:
    """Render the Career Health dashboard."""

    profile = load_profile()

    ats_score = int(
        profile.get(
            "ats_score",
            0,
        )
    )

    skills = profile.get(
        "skills",
        [],
    )

    skill_score = min(
        len(skills) * 10,
        100,
    )

    internship_score = int(
        (
            ats_score
            + skill_score
        )
        / 2
    )

    ai_readiness = 95

    career_score = int(
        (
            ats_score
            + skill_score
            + internship_score
            + ai_readiness
        )
        / 4
    )


    # ========================================================
    # HEADER
    # ========================================================

    st.markdown(
        "## 💚 Career Health"
    )

    st.caption(
        "A live estimate of your overall career readiness."
    )


    # ========================================================
    # MAIN CARD
    # ========================================================

    with st.container(
        border=True,
    ):

        st.metric(
            "Overall Career Health",
            f"{career_score} / 100",
        )

        st.progress(
            career_score / 100
        )

        st.write("")

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

        _progress_row(
            "AI Readiness",
            ai_readiness,
            "🤖",
        )


    # ========================================================
    # STATUS
    # ========================================================

    if career_score >= 80:

        st.success(
            "🚀 You're looking internship-ready. "
            "Now focus on applications and interview preparation."
        )

    elif career_score >= 60:

        st.info(
            "📈 You're building a strong foundation. "
            "Keep improving your resume, skills and projects."
        )

    else:

        st.warning(
            "🌱 Your foundation is still developing. "
            "Start with your resume and core skills."
        )