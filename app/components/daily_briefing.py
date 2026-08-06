import streamlit as st
from datetime import datetime
from app.storage.profile_manager import load_profile


def greeting():

    hour = datetime.now().hour

    if hour < 12:
        return "🌅 Good Morning"

    elif hour < 17:
        return "☀️ Good Afternoon"

    else:
        return "🌙 Good Evening"


def show():

    profile = load_profile()

    ats = profile.get("ats_score", 0)
    skills = profile.get("skills", [])

    st.markdown("## ✨ AI Daily Briefing")

    with st.container(border=True):

        st.markdown(f"### {greeting()}")

        st.caption("Your personalized career update")

        st.write("")

        if ats < 70:
            st.warning(
                "🎯 Your ATS score needs improvement. Optimize keywords in your resume."
            )

        elif ats < 85:
            st.info(
                "🚀 Your resume is strong. Small improvements can make it stand out."
            )

        else:
            st.success(
                "🔥 Excellent! Your resume is highly competitive."
            )

        st.write("")

        if len(skills) < 8:

            st.info(
                "📚 Today's Mission: Learn one new technical skill."
            )

        else:

            st.success(
                "💪 Great skill portfolio. Time to build more projects."
            )

        st.write("")

        st.markdown("### 💡 AI Suggestion")

        st.info(
            """
Focus on:

• Docker

• FastAPI

• GitHub Portfolio

• System Design Basics

These skills will significantly improve internship opportunities.
"""
        )

        st.write("")

        st.markdown("### ⭐ Quote of the Day")

        st.success(
            '"Consistency beats intensity. Build something every single day."'
        )