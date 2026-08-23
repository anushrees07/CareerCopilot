import streamlit as st
from datetime import datetime

from app.storage.profile_manager import load_profile


# ============================================================
# CAREERCOPILOT DAILY BRIEFING
# PREMIUM DASHBOARD COMPONENT
# ============================================================


def greeting():
    """
    Return a time-based greeting.
    """

    hour = datetime.now().hour

    if hour < 12:
        return "🌅 Good Morning"

    elif hour < 17:
        return "☀️ Good Afternoon"

    return "🌙 Good Evening"


def get_ats_message(ats):
    """
    Generate the existing ATS-based recommendation.
    """

    if ats < 70:
        return (
            "🎯 Your ATS score needs improvement. "
            "Optimize keywords in your resume."
        )

    elif ats < 85:
        return (
            "🚀 Your resume is strong. "
            "Small improvements can make it stand out."
        )

    return (
        "🔥 Excellent! Your resume is highly competitive."
    )


def get_skill_message(skills):
    """
    Generate the existing skill-based recommendation.
    """

    if len(skills) < 8:
        return (
            "📚 Today's Mission: "
            "Learn one new technical skill."
        )

    return (
        "💪 Great skill portfolio. "
        "Time to build more projects."
    )


def show():
    """
    Premium AI Daily Briefing.

    Existing profile-driven logic is preserved.
    Styling is handled by the global UI/CSS system.
    """

    # ========================================================
    # LOAD PROFILE
    # ========================================================

    profile = load_profile()

    ats = profile.get("ats_score", 0)

    skills = profile.get(
        "skills",
        [],
    )

    # ========================================================
    # SECTION HEADER
    # ========================================================

    st.markdown(
        "## ✨ AI Daily Briefing"
    )

    st.caption(
        "Personalized career intelligence based on your current profile."
    )

    st.write("")

    # ========================================================
    # MAIN BRIEFING CARD
    # ========================================================

    with st.container(
        border=True,
        key="daily_briefing",
    ):

        # ====================================================
        # GREETING
        # ====================================================

        st.markdown(
            f"### {greeting()}"
        )

        st.caption(
            "Your personalized career update"
        )

        st.write("")

        # ====================================================
        # ATS + SKILLS
        # ====================================================

        col1, col2 = st.columns(
            2,
            gap="medium",
        )

        # ----------------------------------------------------
        # ATS INSIGHT
        # ----------------------------------------------------

        with col1:

            st.markdown(
                "#### 🎯 Resume Intelligence"
            )

            if ats < 70:

                st.warning(
                    get_ats_message(ats)
                )

            elif ats < 85:

                st.info(
                    get_ats_message(ats)
                )

            else:

                st.success(
                    get_ats_message(ats)
                )

        # ----------------------------------------------------
        # SKILL INSIGHT
        # ----------------------------------------------------

        with col2:

            st.markdown(
                "#### 🧠 Skill Momentum"
            )

            if len(skills) < 8:

                st.info(
                    get_skill_message(skills)
                )

            else:

                st.success(
                    get_skill_message(skills)
                )

        st.write("")

        # ====================================================
        # TODAY'S AI SUGGESTION
        # ====================================================

        st.markdown(
            "### 💡 Today's AI Suggestion"
        )

        st.caption(
            "High-value areas worth adding to your career stack."
        )

        suggestion_col1, suggestion_col2 = st.columns(
            2,
            gap="medium",
        )

        with suggestion_col1:

            st.markdown(
                """
                **🐳 Docker**

                Learn containerization and basic
                Docker workflows for modern development.
                """
            )

            st.markdown(
                """
                **⚡ FastAPI**

                Build lightweight Python APIs and
                strengthen your backend development skills.
                """
            )

        with suggestion_col2:

            st.markdown(
                """
                **🌐 GitHub Portfolio**

                Turn your projects into visible proof
                of your technical abilities.
                """
            )

            st.markdown(
                """
                **🏗️ System Design Basics**

                Start understanding how scalable
                applications are structured.
                """
            )

        st.write("")

        # ====================================================
        # CAREER ACTION
        # ====================================================

        st.markdown(
            "### 🚀 Your Move Today"
        )

        st.info(
            "Pick one skill above and spend at least "
            "30 focused minutes learning or building with it."
        )