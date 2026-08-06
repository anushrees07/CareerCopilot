import streamlit as st

from app.components.hero import show as hero
from app.components.stat_cards import show as stat_cards
from app.components.profile_summary import show as profile_summary
from app.components.quick_actions import show as quick_actions

# These components will be built next.
# Comment them for now if they don't exist yet.

try:
    from app.components.daily_briefing import show as daily_briefing
except Exception:
    daily_briefing = None

try:
    from app.components.career_health_dashboard import (
        show as career_health_dashboard,
    )
except Exception:
    career_health_dashboard = None

try:
    from app.components.ai_assistant_panel import (
        show as ai_assistant_panel,
    )
except Exception:
    ai_assistant_panel = None

try:
    from app.components.footer import show as footer
except Exception:
    footer = None


def show():

    # -------------------------
    # Hero Section
    # -------------------------

    hero()

    st.write("")

    # -------------------------
    # Statistics
    # -------------------------

    stat_cards()

    st.write("")

    # -------------------------
    # Daily Briefing
    # -------------------------

    if daily_briefing:
        daily_briefing()

    st.write("")

    # -------------------------
    # Profile + Career Health
    # -------------------------

    left, right = st.columns([2, 1])

    with left:
        profile_summary()

    with right:

        if career_health_dashboard:
            career_health_dashboard()

    st.write("")

    # -------------------------
    # Quick Actions
    # -------------------------

    quick_actions()

    st.write("")

    # -------------------------
    # AI Assistant
    # -------------------------

    if ai_assistant_panel:
        ai_assistant_panel()

    st.write("")

    # -------------------------
    # Footer
    # -------------------------

    if footer:
        footer()