from __future__ import annotations

import streamlit as st

from app.storage.profile_manager import load_profile


def show() -> None:
    """Render the user's AI-generated career profile."""


    profile = load_profile()

    st.markdown("## 👤 Career Profile")

    st.caption(
        "Your AI-generated career identity based on your resume."
    )

    st.write("")


    # ========================================================
    # EMPTY STATE
    # ========================================================

    if not profile.get("resume_name"):

        with st.container(
            border=True,
        ):

            st.markdown(
                "### 📄 Your Career Profile is Waiting"
            )

            st.write(
                "Upload your resume to unlock personalized "
                "career insights, extracted skills and AI analysis."
            )

            st.write("")

            col1, col2, col3 = st.columns(
                3,
                gap="medium",
            )

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


    # ========================================================
    # RESUME + ATS
    # ========================================================

    with st.container(
        border=True,
    ):

        left, right = st.columns(
            [1.5, 1],
            gap="large",
        )

        with left:

            st.markdown("### 📄 Resume")

            st.success(
                profile.get(
                    "resume_name",
                    "Resume uploaded",
                )
            )

        with right:

            ats_score = profile.get(
                "ats_score",
                0,
            )

            st.metric(
                "🎯 ATS Score",
                f"{ats_score}%",
            )


    st.write("")


    # ========================================================
    # SKILLS
    # ========================================================

    with st.container(
        border=True,
    ):

        st.markdown(
            "### 🧠 Extracted Skills"
        )

        skills = profile.get(
            "skills",
            [],
        )

        if skills:

            skill_columns = st.columns(
                4,
                gap="small",
            )

            for index, skill in enumerate(skills):

                with skill_columns[index % 4]:

                    st.success(
                        skill
                    )

        else:

            st.warning(
                "No skills have been extracted yet."
            )


    st.write("")


    # ========================================================
    # AI SUMMARY
    # ========================================================

    with st.container(
        border=True,
    ):

        st.markdown(
            "### 🤖 AI Career Summary"
        )

        feedback = profile.get(
            "ai_feedback",
            "",
        )

        if feedback:

            st.write(
                feedback
            )

        else:

            st.info(
                "Analyze your resume to receive "
                "AI-powered career insights."
            )