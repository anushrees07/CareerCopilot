import streamlit as st

from app.storage.settings_manager import load_settings
from app.ui.appearance_manager import (
    initialize,
    show_theme_switcher,
    apply_theme,
)

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="CareerCopilot",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# INITIALIZE APPEARANCE
# ============================================================

initialize()

apply_theme()

# ============================================================
# PAGE IMPORTS
# ============================================================

from app.pages import dashboard
from app.pages import resume_analyzer
from app.pages import opportunities
from app.pages import skill_gap
from app.pages import ai_coach
from app.pages import interview_prep
from app.pages import roadmap
from app.pages import analytics
from app.pages import settings
from app.pages import ai_setup


# ============================================================
# PAGE REGISTRY
# ============================================================

PAGES = {
    "🏠 Dashboard": dashboard.show,
    "📄 Resume Analyzer": resume_analyzer.show,
    "💼 Opportunities": opportunities.show,
    "🧠 Skill Gap": skill_gap.show,
    "🤖 AI Coach": ai_coach.show,
    "🎤 Interview Prep": interview_prep.show,
    "🗺️ Roadmap": roadmap.show,
    "📊 Analytics": analytics.show,
    "⚙️ Settings": settings.show,
    "🧠 AI Setup": ai_setup.show,
}


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "🏠 Dashboard"


# ============================================================
# AI CONFIGURATION CHECK
# ============================================================

def is_ai_configured():

    settings_data = load_settings()

    provider = settings_data.get(
        "provider",
        "",
    )

    provider_keys = {
        "Gemini": "gemini_key",
        "OpenAI": "openai_key",
        "Claude": "claude_key",
        "OpenRouter": "openrouter_key",
    }

    key_name = provider_keys.get(provider)

    if not key_name:
        return False

    api_key = settings_data.get(
        key_name,
        "",
    )

    if not isinstance(api_key, str):
        return False

    return bool(api_key.strip())


# ============================================================
# FIRST-LAUNCH AI GATE
# ============================================================

if not is_ai_configured():

    st.session_state.page = "🧠 AI Setup"


# ============================================================
# AI SETUP SCREEN
# ============================================================

if st.session_state.page == "🧠 AI Setup":

    ai_setup.show()

    st.stop()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    # --------------------------------------------------------
    # BRAND
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="cc-sidebar-brand">
            🚀 <strong>CareerCopilot</strong>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.caption(
        "Your AI-powered career companion"
    )

    st.divider()

    # --------------------------------------------------------
    # APPEARANCE
    # --------------------------------------------------------

    show_theme_switcher()

    st.divider()

    # --------------------------------------------------------
    # NAVIGATION
    # --------------------------------------------------------

    navigation_pages = [
        "🏠 Dashboard",
        "📄 Resume Analyzer",
        "💼 Opportunities",
        "🧠 Skill Gap",
        "🤖 AI Coach",
        "🎤 Interview Prep",
        "🗺️ Roadmap",
        "📊 Analytics",
        "⚙️ Settings",
    ]

    for page_name in navigation_pages:

        is_current = (
            st.session_state.page == page_name
        )

        button_type = (
            "primary"
            if is_current
            else "secondary"
        )

        if st.button(
            page_name,
            key=f"nav_{page_name}",
            use_container_width=True,
            type=button_type,
        ):

            st.session_state.page = page_name

            st.rerun()

    st.divider()

    # --------------------------------------------------------
    # AI STATUS
    # --------------------------------------------------------

    current_settings = load_settings()

    current_provider = current_settings.get(
        "provider",
        "Not configured",
    )

    st.markdown(
        "### 🤖 AI Brain"
    )

    if is_ai_configured():

        st.success(
            f"● {current_provider} Connected"
        )

    else:

        st.warning(
            "⚠️ AI Not Configured"
        )

    # --------------------------------------------------------
    # CHANGE AI PROVIDER
    # --------------------------------------------------------

    if st.button(
        "🔄 Change AI Provider",
        use_container_width=True,
    ):

        st.session_state.page = "🧠 AI Setup"

        st.rerun()

    st.write("")

    st.caption(
        "CareerCopilot • AI Career Assistant"
    )


# ============================================================
# MAIN PAGE
# ============================================================

page_function = PAGES.get(
    st.session_state.page
)


# ============================================================
# FALLBACK
# ============================================================

if page_function is None:

    st.session_state.page = "🏠 Dashboard"

    st.rerun()


# ============================================================
# RENDER CURRENT PAGE
# ============================================================

page_function()