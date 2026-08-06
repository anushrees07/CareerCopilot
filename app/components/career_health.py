import streamlit as st

from app.ui.metric_card import metric
from app.ui.section_header import show as section


def show():

    section(
        "📊 Career Health",
        "Your overall career progress at a glance.",
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric(
            "Resume",
            "92%",
            "+4 this week",
            "🎯",
        )

    with c2:
        metric(
            "ATS",
            "89%",
            "+7 keywords",
            "📄",
        )

    with c3:
        metric(
            "Skills",
            "18",
            "Growing",
            "🧠",
        )

    with c4:
        metric(
            "AI",
            "Ready",
            "Connected",
            "🤖",
        )