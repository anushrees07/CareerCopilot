import streamlit as st

from app.storage.profile_manager import load_profile


def show():

    profile = load_profile()

    with st.container(border=True):

        st.subheader("🤖 AI Insights")

        if not profile["resume_name"]:

            st.info(
                "Upload and analyze your resume to receive personalized AI insights."
            )
            return

        st.success("Resume analyzed successfully!")

        st.markdown("### 📌 Current Status")

        st.write(f"**ATS Score:** {profile['ats_score']}%")
        st.write(f"**Career Health:** {profile['career_health']}%")
        st.write(f"**Skills Found:** {len(profile['skills'])}")

        st.markdown("### 💡 AI Recommendation")

        if profile["skills"]:
            st.success(
                "Keep building projects and strengthen the missing skills suggested in your resume analysis."
            )
        else:
            st.warning(
                "No skills have been extracted yet."
            )