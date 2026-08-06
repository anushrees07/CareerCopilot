import streamlit as st

from app.storage.profile_manager import load_profile

from app.ui.metric_card import show as metric_card
from app.ui.progress_card import show as progress_card
from app.ui.section_header import show as section_header
from app.ui.status_badge import show as status_badge


def show():

    profile = load_profile()

    section_header(
        "📊 Career Analytics",
        "Track your career progress with AI insights."
    )

    st.write("")

    c1, c2, c3 = st.columns(3)

    with c1:

        metric_card(
            "ATS Score",
            f"{profile['ats_score']}%",
            "Resume Quality",
            "📄",
        )

    with c2:

        metric_card(
            "Skills",
            str(len(profile["skills"])),
            "Detected",
            "🧠",
        )

    with c3:

        metric_card(
            "Career Health",
            f"{profile['career_health']}%",
            "Overall",
            "🚀",
        )

    st.write("")

    progress_card(
        "Career Health",
        profile["career_health"],
        "Overall career readiness"
    )

    st.divider()

    section_header(
        "🧠 Skills"
    )

    if profile["skills"]:

        cols = st.columns(4)

        for i, skill in enumerate(profile["skills"]):

            with cols[i % 4]:

                status_badge(
                    skill,
                    "purple",
                )

    else:

        st.info(
            "No skills detected yet."
        )

    st.divider()

    section_header(
        "📄 Resume Statistics"
    )

    resume = profile.get(
        "resume_text",
        ""
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        metric_card(
            "Characters",
            str(len(resume)),
            "",
            "📃",
        )

    with c2:

        metric_card(
            "Words",
            str(len(resume.split())),
            "",
            "📝",
        )

    with c3:

        metric_card(
            "Resume",
            "Uploaded" if profile["resume_name"] else "Missing",
            profile["resume_name"],
            "📂",
        )

    st.divider()

    section_header(
        "📅 Activity Timeline"
    )

    if profile["resume_name"]:

        status_badge(
            "Resume Uploaded",
            "green",
        )

    if profile["skills"]:

        status_badge(
            "Skills Extracted",
            "blue",
        )

    if profile["ats_score"]:

        status_badge(
            "ATS Calculated",
            "purple",
        )

    if profile["career_health"]:

        status_badge(
            "Career Health Updated",
            "yellow",
        )