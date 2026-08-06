import streamlit as st
from app.storage.profile_manager import load_profile


def show():

    profile = load_profile()

    ats = profile.get("ats_score", 0)
    skills = len(profile.get("skills", []))
    health = profile.get("career_health", 0)
    resume = profile.get("resume_name", "")

    st.markdown("### 📊 Career Metrics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        with st.container(border=True):
            st.metric(
                "🎯 ATS Score",
                f"{ats}%",
                delta="+8"
            )

    with col2:
        with st.container(border=True):
            st.metric(
                "🧠 Skills",
                skills,
                delta="+2"
            )

    with col3:
        with st.container(border=True):
            st.metric(
                "💚 Career Health",
                f"{health}%",
                delta="+5"
            )

    with col4:
        with st.container(border=True):

            status = "Uploaded ✅" if resume else "Not Uploaded"

            st.metric(
                "📄 Resume",
                status
            )