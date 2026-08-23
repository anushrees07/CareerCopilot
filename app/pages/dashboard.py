import streamlit as st

from app.components.hero import show as hero
from app.components.stat_cards import show as stat_cards
from app.components.profile_summary import show as profile_summary
from app.components.quick_actions import show as quick_actions


# ============================================================
# OPTIONAL COMPONENTS
# ============================================================

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


# ============================================================
# DASHBOARD
# ============================================================

def show():
    """
    CareerCopilot main dashboard.

    Layout philosophy:
        Hero
        ↓
        Career Metrics
        ↓
        Daily Briefing
        ↓
        Profile + Career Health
        ↓
        Quick Actions
        ↓
        AI Assistant
        ↓
        Footer

    Existing components and functionality are preserved.
    """

    # ========================================================
    # HERO
    # ========================================================

    hero()


    # ========================================================
    # CAREER METRICS
    # ========================================================

    stat_cards()


    # ========================================================
    # DAILY BRIEFING
    # ========================================================

    if daily_briefing:

        st.write("")

        daily_briefing()


    # ========================================================
    # PROFILE + CAREER HEALTH
    # ========================================================

    if profile_summary or career_health_dashboard:

        st.write("")

        left, right = st.columns(
            [2, 1],
            gap="large",
        )


        # ----------------------------------------------------
        # PROFILE
        # ----------------------------------------------------

        with left:

            profile_summary()


        # ----------------------------------------------------
        # CAREER HEALTH
        # ----------------------------------------------------

        with right:

            if career_health_dashboard:

                career_health_dashboard()


    # ========================================================
    # QUICK ACTIONS
    # ========================================================

    st.write("")

    quick_actions()


    # ========================================================
    # AI ASSISTANT
    # ========================================================

    if ai_assistant_panel:

        st.write("")

        ai_assistant_panel()


    # ========================================================
    # FOOTER
    # ========================================================

    if footer:

        st.write("")

        footer()