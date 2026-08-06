import streamlit as st
from app.storage.profile_manager import load_profile


def show():

    profile = load_profile()

    st.markdown("## 👤 Career Profile")

    if not profile.get("resume_name"):

        st.info(
            "📄 Upload your resume to generate your personalized career profile."
        )

        return

    st.success(f"Resume: **{profile['resume_name']}**")

    st.write("")

    st.markdown("### 🧠 Extracted Skills")

    skills = profile.get("skills", [])

    if skills:

        cols = st.columns(4)

        for i, skill in enumerate(skills):

            with cols[i % 4]:
                st.success(skill)

    else:

        st.warning("No skills extracted yet.")

    st.write("")

    st.markdown("### 🤖 AI Career Summary")

    feedback = profile.get("ai_feedback", "")

    if feedback:
        st.write(feedback)
    else:
        st.info(
            "Analyze your resume to receive AI-powered career insights."
        )