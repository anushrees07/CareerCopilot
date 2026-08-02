from app.ui.styles import load_css
import streamlit as st

st.set_page_config(
    page_title="CareerCopilot",
    page_icon="🚀",
    layout="wide"
)
load_css()

st.sidebar.title("🚀 CareerCopilot")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "🤖 AI Setup",
        "📄 Resume Analysis",
        "💼 Internship Matches",
        "ℹ️ About"
    ]
)

if page == "🏠 Dashboard":
    from app.pages.home import show
    show()

elif page == "🤖 AI Setup":
    from app.pages.setup import show
    show()

elif page == "📄 Resume Analysis":
    from app.pages.results import show
    show()

elif page == "💼 Internship Matches":
    st.title("💼 Internship Matches")
    st.info("Coming soon...")

elif page == "ℹ️ About":
    st.title("About CareerCopilot")
    st.write("AI-powered career assistant.")