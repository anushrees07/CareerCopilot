import streamlit as st

from app.storage.profile_manager import load_profile


def show():

    profile = load_profile()

    st.markdown("## 👤 Career Profile")

    st.caption(
        "Your AI-generated career identity based on your resume."
    )

    st.write("")

    # ========================================================
    # NO RESUME STATE
    # ========================================================

    if not profile.get("resume_name"):

        with st.container(
            border=True,
            key="career-profile-empty",
        ):

            st.markdown("### 📄 Your Career Profile is Waiting")

            st.write(
                "Upload your resume to unlock your personalized "
                "career profile, extracted skills and AI insights."
            )

            st.write("")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown("📊")
                st.caption("ATS Insights")

            with col2:
                st.markdown("🧠")
                st.caption("Skill Intelligence")

            with col3:
                st.markdown("🤖")
                st.caption("AI Career Summary")

        return

    # ========================================================
    # RESUME INFORMATION
    # ========================================================

    with st.container(
        border=True,
        key="career-profile-main",
    ):

        col1, col2 = st.columns(
            [1.4, 1],
            gap="large",
        )

        with col1:

            st.markdown("### 📄 Resume")

            st.success(
                f"**{profile['resume_name']}**"
            )

        with col2:

            ats = profile.get("ats_score", 0)

            st.metric(
                "🎯 ATS Score",
                f"{ats}%",
            )

    st.write("")

    # ========================================================
    # SKILLS
    # ========================================================

    with st.container(
        border=True,
        key="career-profile-skills",
    ):

        st.markdown("### 🧠 Extracted Skills")

        skills = profile.get("skills", [])

        if skills:

            cols = st.columns(4)

            for i, skill in enumerate(skills):

                with cols[i % 4]:

                    st.success(
                        skill
                    )

        else:

            st.warning(
                "No skills extracted yet."
            )

    st.write("")

    # ========================================================
    # AI SUMMARY
    # ========================================================

    with st.container(
        border=True,
        key="career-profile-ai",
    ):

        st.markdown("### 🤖 AI Career Summary")

        feedback = profile.get(
            "ai_feedback",
            "",
        )

        if feedback:

            st.write(feedback)

        else:

            st.info(
                "Analyze your resume to receive "
                "AI-powered career insights."
            )