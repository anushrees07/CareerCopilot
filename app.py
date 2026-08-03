import streamlit as st

from app.ui.theme import load_theme

from app.pages.dashboard import show as dashboard_page
from app.pages.resume import show as resume_page
from app.pages.internships import show as internships_page
from app.pages.ai_chat import show as ai_chat_page
from app.pages.settings import show as settings_page


st.set_page_config(
    page_title="CareerCopilot",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

load_theme()

pages = {
    "🏠 Dashboard": dashboard_page,
    "📄 Resume": resume_page,
    "💼 Internships": internships_page,
    "🤖 AI Coach": ai_chat_page,
    "⚙️ Settings": settings_page,
}

st.sidebar.title("🚀 CareerCopilot")

selected = st.sidebar.radio(
    "Navigation",
    list(pages.keys()),
)

pages[selected]()