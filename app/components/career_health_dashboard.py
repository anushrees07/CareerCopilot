import streamlit as st
from app.storage.profile_manager import load_profile


def progress(label, value, color="🟢"):
    st.markdown(f"**{color} {label}**")
    st.progress(value / 100)
    st.caption(f"{value}%")
    st.write("")


def show():

    profile = load_profile()

    ats = profile.get("ats_score", 72)
    skills = profile.get("skills", [])

    skill_score = min(len(skills) * 10, 100)

    internship = min(int((ats + skill_score) / 2), 100)

    career = int((ats + skill_score + internship) / 3)

    st.markdown("## 💚 Career Health")

    with st.container(border=True):

        st.metric(
            "Overall Career Health",
            f"{career}%"
        )

        st.write("")

        progress("Resume Strength", ats)

        progress("Skill Readiness", skill_score)

        progress("Internship Readiness", internship)

        progress(
            "AI Readiness",
            95,
            "🤖"
        )

        st.success(
            "You're on the right path. Keep improving your portfolio and projects."
        )