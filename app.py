import streamlit as st

# ==============================
# UI
# ==============================
from app.ui.theme import load_theme

# ==============================
# Pages
# ==============================
from app.pages import (
    dashboard,
    resume_analyzer,
    opportunities,
    skill_gap,
    ai_coach,
    interview_prep,
    roadmap,
    analytics,
    settings,
)

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(
    page_title="CareerCopilot",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ==============================
# LOAD THEME
# ==============================
load_theme()

# ==============================
# PAGE REGISTRY
# ==============================
PAGES = {
    "🏠 Dashboard": dashboard.show,
    "📄 Resume Analyzer": resume_analyzer.show,
    "💼 Opportunities": opportunities.show,
    "🧠 Skill Gap": skill_gap.show,
    "🤖 AI Coach": ai_coach.show,
    "🎤 Interview Prep": interview_prep.show,
    "🗺 Roadmap": roadmap.show,
    "📊 Analytics": analytics.show,
    "⚙ Settings": settings.show,
}

# ==============================
# SESSION STATE
# ==============================
if "page" not in st.session_state:
    st.session_state.page = "🏠 Dashboard"

# If an invalid page somehow gets stored
if st.session_state.page not in PAGES:
    st.session_state.page = "🏠 Dashboard"

# ==============================
# SIDEBAR
# ==============================
st.sidebar.markdown("# 🚀 CareerCopilot")
st.sidebar.caption("AI Powered Career Platform")

selected_page = st.sidebar.radio(
    "Navigation",
    list(PAGES.keys()),
    index=list(PAGES.keys()).index(st.session_state.page),
)

# Update page if user clicks sidebar
if selected_page != st.session_state.page:
    st.session_state.page = selected_page
    st.rerun()

# ==============================
# PAGE RENDER
# ==============================
PAGES[st.session_state.page]()