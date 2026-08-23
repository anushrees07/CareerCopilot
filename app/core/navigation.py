from __future__ import annotations

import streamlit as st


# ============================================================
# CAREERCOPILOT NAVIGATION
# ============================================================
#
# This module is the single source of truth for application
# navigation.
#
# Pages use stable internal IDs.
# UI components use human-readable labels.
#
# Example:
#
#     RESUME_ANALYZER
#         ↓
#     "resume_analyzer"
#
# This prevents UI text changes from breaking navigation.
# ============================================================


# ============================================================
# PAGE IDENTIFIERS
# ============================================================

DASHBOARD = "dashboard"
RESUME_ANALYZER = "resume_analyzer"
OPPORTUNITIES = "opportunities"
SKILL_GAP = "skill_gap"
AI_COACH = "ai_coach"
INTERVIEW_PREP = "interview_prep"
ROADMAP = "roadmap"
ANALYTICS = "analytics"
SETTINGS = "settings"
AI_SETUP = "ai_setup"


# Default page shown after successful AI setup
DEFAULT_PAGE = DASHBOARD


# ============================================================
# PAGE LABELS
# ============================================================

PAGE_LABELS = {
    DASHBOARD: "🚀 Dashboard",
    RESUME_ANALYZER: "📄 Resume Analyzer",
    OPPORTUNITIES: "💼 Opportunities",
    SKILL_GAP: "🧩 Skill Gap",
    AI_COACH: "🤖 AI Coach",
    INTERVIEW_PREP: "🎤 Interview Prep",
    ROADMAP: "🗺️ Roadmap",
    ANALYTICS: "📊 Analytics",
    SETTINGS: "⚙️ Settings",
    AI_SETUP: "🧩 AI Setup",
}


# ============================================================
# MAIN NAVIGATION ORDER
# ============================================================

NAVIGATION_PAGES = (
    DASHBOARD,
    RESUME_ANALYZER,
    OPPORTUNITIES,
    SKILL_GAP,
    AI_COACH,
    INTERVIEW_PREP,
    ROADMAP,
    ANALYTICS,
    SETTINGS,
)


# ============================================================
# NAVIGATION STATE
# ============================================================

def initialize() -> None:
    """
    Initialize the application's navigation state.

    Navigation state is stored using an internal page ID,
    never a display label.
    """

    current_page = st.session_state.get("page")

    if current_page not in PAGE_LABELS:
        st.session_state.page = DEFAULT_PAGE


# ============================================================
# CURRENT PAGE
# ============================================================

def get_current_page() -> str:
    """
    Return the current internal page ID.
    """

    initialize()

    return st.session_state.page


# ============================================================
# NAVIGATE
# ============================================================

def navigate(page: str) -> None:
    """
    Navigate to a valid CareerCopilot page.

    Parameters
    ----------
    page:
        Internal page identifier such as RESUME_ANALYZER.

    Raises
    ------
    ValueError
        If an unknown page identifier is supplied.
    """

    if page not in PAGE_LABELS:

        raise ValueError(
            f"Unknown CareerCopilot page: {page}"
        )

    st.session_state.page = page


# ============================================================
# PAGE LABEL
# ============================================================

def get_label(page: str) -> str:
    """
    Return the human-readable label for a page.
    """

    if page not in PAGE_LABELS:

        raise ValueError(
            f"Unknown CareerCopilot page: {page}"
        )

    return PAGE_LABELS[page]


# ============================================================
# NAVIGATION PAGES
# ============================================================

def get_navigation_pages() -> list[str]:
    """
    Return pages displayed in the primary application
    navigation.

    AI Setup is intentionally excluded because it is a
    configuration flow rather than a normal application page.
    """

    return list(NAVIGATION_PAGES)


# ============================================================
# PAGE VALIDATION
# ============================================================

def is_valid_page(page: str) -> bool:
    """
    Check whether a page identifier is registered.
    """

    return page in PAGE_LABELS


# ============================================================
# PAGE DISPLAY LABELS
# ============================================================

def get_all_page_labels() -> dict[str, str]:
    """
    Return a copy of the complete page-label registry.

    Returning a copy prevents accidental mutation of the
    navigation registry from another module.
    """

    return PAGE_LABELS.copy()