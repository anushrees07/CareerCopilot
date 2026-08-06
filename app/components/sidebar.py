import streamlit as st

from app.storage.profile_manager import load_profile


def nav_button(label, page, icon):

    if st.button(

        f"{icon}  {label}",

        use_container_width=True,

        key=page,

    ):

        st.session_state.page = page

        st.rerun()


def show():

    profile = load_profile()

    st.sidebar.markdown("# 🚀 CareerCopilot")

    st.sidebar.caption(
        "Build Your Dream Career"
    )

    st.sidebar.divider()

    st.sidebar.subheader("👤 Profile")

    if profile["resume_name"]:

        st.sidebar.success("Resume Uploaded")

        st.sidebar.write(profile["resume_name"])

    else:

        st.sidebar.warning("No Resume")

    st.sidebar.metric(

        "ATS Score",

        f"{profile['ats_score']}%",

    )

    st.sidebar.metric(

        "Skills",

        len(profile["skills"]),

    )

    st.sidebar.divider()

    nav_button(

        "Dashboard",

        "Dashboard",

        "🏠",

    )

    nav_button(

        "Resume Intelligence",

        "Resume Analyzer",

        "📄",

    )

    nav_button(

        "Opportunities",

        "Opportunities",

        "💼",

    )

    nav_button(

        "AI Coach",

        "AI Coach",

        "🤖",

    )

    nav_button(

        "Interview Prep",

        "Interview Prep",

        "🎤",

    )

    nav_button(

        "Roadmap",

        "Roadmap",

        "🗺",

    )

    nav_button(

        "Analytics",

        "Analytics",

        "📊",

    )

    nav_button(

        "Settings",

        "Settings",

        "⚙",

    )

    st.sidebar.divider()

    st.sidebar.progress(

        profile["career_health"] / 100

    )

    st.sidebar.caption(

        f"Career Health : {profile['career_health']}%"

    )

    st.sidebar.divider()

    st.sidebar.caption(
        "✨ Powered by AI"
    )