import streamlit as st


# ============================================================
# CAREERCOPILOT APPEARANCE MANAGER
# ============================================================


def initialize():
    """
    Initialize the CareerCopilot appearance system.
    """

    if "appearance" not in st.session_state:
        st.session_state.appearance = "dark"


def get_current_theme():
    """
    Return the currently selected appearance.
    """

    return st.session_state.get(
        "appearance",
        "dark",
    )


# ============================================================
# LIGHT THEME
# ============================================================

LIGHT_THEME_CSS = """

/* ============================================================
   LIGHT THEME ROOT
   ============================================================ */

[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(99, 102, 241, 0.14),
            transparent 32%
        ),
        radial-gradient(
            circle at 90% 15%,
            rgba(6, 182, 212, 0.16),
            transparent 30%
        ),
        radial-gradient(
            circle at 50% 90%,
            rgba(168, 85, 247, 0.10),
            transparent 35%
        ),
        linear-gradient(
            135deg,
            #f8fbff 0%,
            #eef4ff 45%,
            #f8f5ff 100%
        ) !important;
}


/* ============================================================
   MAIN CONTENT
   ============================================================ */

[data-testid="stMain"] {
    background: transparent !important;
}

.main {
    background: transparent !important;
}


/* ============================================================
   HEADINGS
   ============================================================ */

[data-testid="stAppViewContainer"] h1,
[data-testid="stAppViewContainer"] h2,
[data-testid="stAppViewContainer"] h3,
[data-testid="stAppViewContainer"] h4 {
    color: #111827 !important;
    text-shadow: none !important;
}


/* Hero heading */

.cc-title,
.hero-title,
.main-title {
    color: #111827 !important;

    text-shadow:
        0 4px 20px rgba(79, 70, 229, 0.12) !important;
}


/* Highlighted hero word */

.cc-title span,
.hero-title span,
.main-title span {
    color: #0891b2 !important;

    text-shadow:
        0 4px 20px rgba(6, 182, 212, 0.28) !important;
}


/* Subtitles */

.cc-subtitle,
.hero-subtitle {
    color: #475569 !important;
}


/* Normal markdown */

[data-testid="stMarkdownContainer"] p {
    color: #475569 !important;
}


/* Captions */

[data-testid="stCaptionContainer"] {
    color: #64748b !important;
}


/* ============================================================
   GLASSMORPHIC CONTAINERS
   ============================================================ */

[data-testid="stVerticalBlockBorderWrapper"] {

    background:
        linear-gradient(
            135deg,
            rgba(255, 255, 255, 0.72),
            rgba(255, 255, 255, 0.42)
        ) !important;

    border:
        1px solid rgba(255, 255, 255, 0.85) !important;

    border-radius: 24px !important;

    box-shadow:
        0 20px 50px rgba(15, 23, 42, 0.08),
        0 4px 18px rgba(79, 70, 229, 0.06),
        inset 0 1px 0 rgba(255, 255, 255, 0.9) !important;

    backdrop-filter: blur(24px) saturate(160%) !important;

    -webkit-backdrop-filter: blur(24px) saturate(160%) !important;

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease,
        border-color 0.25s ease !important;
}


/* Card hover */

[data-testid="stVerticalBlockBorderWrapper"]:hover {

    transform: translateY(-3px) !important;

    border-color:
        rgba(99, 102, 241, 0.28) !important;

    box-shadow:
        0 25px 60px rgba(15, 23, 42, 0.10),
        0 8px 28px rgba(99, 102, 241, 0.12),
        inset 0 1px 0 rgba(255, 255, 255, 1) !important;
}


/* ============================================================
   GLOWING BUTTONS
   ============================================================ */

[data-testid="stButton"] button {

    border-radius: 14px !important;

    border:
        1px solid rgba(99, 102, 241, 0.18) !important;

    background:
        linear-gradient(
            135deg,
            #8b5cf6 0%,
            #6366f1 48%,
            #3b82f6 100%
        ) !important;

    color: #ffffff !important;

    font-weight: 700 !important;

    box-shadow:
        0 8px 25px rgba(99, 102, 241, 0.22),
        0 0 20px rgba(99, 102, 241, 0.10) !important;

    transition:
        transform 0.2s ease,
        box-shadow 0.2s ease,
        filter 0.2s ease !important;
}


/* Button hover */

[data-testid="stButton"] button:hover {

    transform: translateY(-2px) !important;

    filter: brightness(1.06) !important;

    box-shadow:
        0 12px 32px rgba(99, 102, 241, 0.30),
        0 0 28px rgba(99, 102, 241, 0.20) !important;
}


/* Button active */

[data-testid="stButton"] button:active {

    transform: translateY(0) !important;
}


/* ============================================================
   SECONDARY / NAV BUTTONS
   ============================================================ */

[data-testid="stButton"] button[kind="secondary"] {

    background:
        rgba(255, 255, 255, 0.58) !important;

    color:
        #1e293b !important;

    border:
        1px solid rgba(100, 116, 139, 0.18) !important;

    box-shadow:
        0 8px 24px rgba(15, 23, 42, 0.06),
        inset 0 1px 0 rgba(255, 255, 255, 0.9) !important;

    backdrop-filter: blur(16px) !important;

    -webkit-backdrop-filter: blur(16px) !important;
}


/* Secondary hover */

[data-testid="stButton"] button[kind="secondary"]:hover {

    background:
        rgba(255, 255, 255, 0.82) !important;

    color:
        #4f46e5 !important;

    border-color:
        rgba(99, 102, 241, 0.28) !important;

    box-shadow:
        0 10px 28px rgba(99, 102, 241, 0.12) !important;
}


/* ============================================================
   PRIMARY BUTTON
   ============================================================ */

[data-testid="stButton"] button[kind="primary"] {

    background:
        linear-gradient(
            135deg,
            #06b6d4,
            #3b82f6,
            #6366f1
        ) !important;

    color: white !important;

    border:
        1px solid rgba(255, 255, 255, 0.35) !important;

    box-shadow:
        0 8px 30px rgba(59, 130, 246, 0.28),
        0 0 25px rgba(6, 182, 212, 0.14) !important;
}


/* ============================================================
   METRIC CARDS
   ============================================================ */

[data-testid="stMetric"] {

    background:
        rgba(255, 255, 255, 0.58) !important;

    border:
        1px solid rgba(255, 255, 255, 0.80) !important;

    border-radius: 20px !important;

    padding: 20px !important;

    box-shadow:
        0 15px 35px rgba(15, 23, 42, 0.07),
        inset 0 1px 0 rgba(255, 255, 255, 0.9) !important;

    backdrop-filter: blur(18px) !important;

    -webkit-backdrop-filter: blur(18px) !important;
}


/* Metric labels */

[data-testid="stMetricLabel"] {
    color: #64748b !important;
}


/* Metric values */

[data-testid="stMetricValue"] {
    color: #111827 !important;
}


/* ============================================================
   INPUTS
   ============================================================ */

[data-testid="stTextInput"] input,
[data-testid="stTextArea"] textarea,
[data-testid="stFileUploader"] section {

    background:
        rgba(255, 255, 255, 0.58) !important;

    color:
        #111827 !important;

    border:
        1px solid rgba(100, 116, 139, 0.18) !important;

    border-radius:
        14px !important;

    backdrop-filter:
        blur(16px) !important;

    -webkit-backdrop-filter:
        blur(16px) !important;
}


/* ============================================================
   SELECTBOX / RADIO
   ============================================================ */

[data-testid="stSelectbox"] > div,
[data-testid="stRadio"] {

    color:
        #1e293b !important;
}


/* ============================================================
   DIVIDERS
   ============================================================ */

[data-testid="stDivider"] {
    border-color:
        rgba(100, 116, 139, 0.14) !important;
}


/* ============================================================
   SIDEBAR
   ============================================================ */

section[data-testid="stSidebar"] {

    background:
        linear-gradient(
            180deg,
            rgba(248, 250, 252, 0.94),
            rgba(239, 246, 255, 0.94)
        ) !important;

    border-right:
        1px solid rgba(100, 116, 139, 0.12) !important;

    box-shadow:
        8px 0 40px rgba(15, 23, 42, 0.06) !important;

    backdrop-filter:
        blur(24px) !important;

    -webkit-backdrop-filter:
        blur(24px) !important;
}


/* Sidebar text */

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span {

    color:
        #1e293b !important;
}


/* Sidebar caption */

section[data-testid="stSidebar"]
[data-testid="stCaptionContainer"] {

    color:
        #64748b !important;
}


/* ============================================================
   SUCCESS / WARNING / INFO
   ============================================================ */

[data-testid="stAlert"] {

    border-radius:
        16px !important;

    backdrop-filter:
        blur(14px) !important;

    -webkit-backdrop-filter:
        blur(14px) !important;
}


/* ============================================================
   SCROLLBAR
   ============================================================ */

::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: transparent;
}

::-webkit-scrollbar-thumb {

    background:
        linear-gradient(
            180deg,
            #6366f1,
            #06b6d4
        );

    border-radius:
        20px;
}


/* ============================================================
   THEME LABEL
   ============================================================ */

.cc-theme-label {

    color:
        #334155 !important;

    font-size:
        0.85rem;

    font-weight:
        700;

    margin-bottom:
        8px;
}
"""


# ============================================================
# THEME SWITCHER
# ============================================================

def show_theme_switcher():

    current_theme = get_current_theme()

    st.markdown(
        """
        <div class="cc-theme-label">
            Appearance
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🌙 Dark",
            key="theme_dark",
            use_container_width=True,
            type=(
                "primary"
                if current_theme == "dark"
                else "secondary"
            ),
        ):

            st.session_state.appearance = "dark"

            st.rerun()

    with col2:

        if st.button(
            "☀️ Light",
            key="theme_light",
            use_container_width=True,
            type=(
                "primary"
                if current_theme == "light"
                else "secondary"
            ),
        ):

            st.session_state.appearance = "light"

            st.rerun()


# ============================================================
# APPLY THEME
# ============================================================

def apply_theme():

    theme = get_current_theme()

    # --------------------------------------------------------
    # IMPORTANT:
    # We ONLY inject additional CSS for LIGHT mode.
    #
    # This means your existing DARK CSS remains untouched.
    # --------------------------------------------------------

    if theme == "light":

        st.markdown(
            f"""
            <style>
            {LIGHT_THEME_CSS}
            </style>
            """,
            unsafe_allow_html=True,
        )