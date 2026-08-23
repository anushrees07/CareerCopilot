import streamlit as st

from app.storage.settings_manager import load_settings

from app.ui.theme import load_theme

from app.ui.appearance_manager import (
    initialize as initialize_appearance,
    show_theme_switcher,
    apply_theme,
)

from app.core.navigation import (
    initialize as initialize_navigation,
    get_current_page,
    get_navigation_pages,
    get_label,
    navigate,
    DASHBOARD,
    AI_SETUP,
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
# INITIALIZATION
# ============================================================

initialize_appearance()
initialize_navigation()

load_theme()
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

    DASHBOARD:
        dashboard.show,

    "resume_analyzer":
        resume_analyzer.show,

    "opportunities":
        opportunities.show,

    "skill_gap":
        skill_gap.show,

    "ai_coach":
        ai_coach.show,

    "interview_prep":
        interview_prep.show,

    "roadmap":
        roadmap.show,

    "analytics":
        analytics.show,

    "settings":
        settings.show,

    AI_SETUP:
        ai_setup.show,
}


# ============================================================
# AI CONFIGURATION
# ============================================================

def is_ai_configured() -> bool:

    settings_data = load_settings()

    provider = settings_data.get(
        "provider",
        "",
    )

    provider_keys = {

        "Gemini":
            "gemini_key",

        "OpenAI":
            "openai_key",

        "Claude":
            "claude_key",

        "OpenRouter":
            "openrouter_key",
    }

    key_name = provider_keys.get(
        provider
    )

    if not key_name:
        return False

    api_key = settings_data.get(
        key_name,
        "",
    )

    if not isinstance(
        api_key,
        str,
    ):
        return False

    return bool(
        api_key.strip()
    )


# ============================================================
# FIRST LAUNCH AI GATE
# ============================================================

if not is_ai_configured():

    navigate(AI_SETUP)


# ============================================================
# AI SETUP PAGE
# ============================================================

if get_current_page() == AI_SETUP:

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
            🚀 CareerCopilot
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

    for page in get_navigation_pages():

        label = get_label(page)

        current = (
            get_current_page()
            == page
        )

        if st.button(
            label,
            key=f"nav_{page}",
            use_container_width=True,
            type=(
                "primary"
                if current
                else "secondary"
            ),
        ):

            navigate(page)

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
    # CHANGE PROVIDER
    # --------------------------------------------------------

    if st.button(
        "🔄 Change AI Provider",
        use_container_width=True,
    ):

        navigate(AI_SETUP)

        st.rerun()

    st.write("")

    # --------------------------------------------------------
    # FOOTER
    # --------------------------------------------------------

    st.caption(
        "CareerCopilot • AI Career Assistant"
    )


# ============================================================
# CURRENT PAGE
# ============================================================

current_page = get_current_page()

page_function = PAGES.get(
    current_page
)


# ============================================================
# FALLBACK
# ============================================================

if page_function is None:

    navigate(DASHBOARD)

    st.rerun()


# ============================================================
# RENDER
# ============================================================

page_function()