import streamlit as st

from app.core.navigation import navigate


# ============================================================
# CAREERCOPILOT HERO
# ============================================================


def show():

    # ========================================================
    # HERO WRAPPER
    # ========================================================

    st.markdown(
        '<div class="cc-hero">',
        unsafe_allow_html=True,
    )

    left, right = st.columns(
        [1.72, 1],
        gap="large",
    )

    # ========================================================
    # LEFT SIDE
    # ========================================================

    with left:

        st.markdown(
            """
            <div class="cc-hero-left">

                <div class="cc-hero-badge">
                    ✨ &nbsp; AI POWERED CAREER PLATFORM
                </div>

                <div class="cc-hero-title">

                    <span class="cc-hero-line-one">
                        Build Your Dream
                    </span>

                    <span class="cc-hero-line-two">
                        <span class="cc-career-highlight">
                            Career
                        </span>
                        &nbsp;With AI
                    </span>

                </div>

                <div class="cc-hero-description">
                    Analyze your resume, discover internships,
                    identify skill gaps, prepare for interviews,
                    generate career roadmaps, and accelerate
                    your career using your favourite AI provider.
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="cc-hero-actions">',
            unsafe_allow_html=True,
        )

        col1, col2 = st.columns(
            2,
            gap="small",
        )

        with col1:

            if st.button(
                "📄  Analyze Resume",
                key="hero_analyze_resume",
                use_container_width=True,
                type="primary",
            ):

                navigate("resume_analyzer")
                st.rerun()

        with col2:

            if st.button(
                "💼  Explore Opportunities",
                key="hero_opportunities",
                use_container_width=True,
                type="primary",
            ):

                navigate("opportunities")
                st.rerun()

        st.markdown(
            "</div>",
            unsafe_allow_html=True,
        )

    # ========================================================
    # RIGHT SIDE
    # ========================================================

    with right:

        st.markdown(
            """
            <div class="cc-snapshot">

                <div class="cc-snapshot-title">
                    🚀 Career Snapshot
                </div>

                <div class="cc-snapshot-subtitle">
                    Your AI-powered career overview
                </div>

                <div class="cc-snapshot-item">
                    <div class="cc-snapshot-icon">📄</div>
                    <div>Resume Intelligence</div>
                </div>

                <div class="cc-snapshot-item">
                    <div class="cc-snapshot-icon">🤖</div>
                    <div>Multi-AI Providers</div>
                </div>

                <div class="cc-snapshot-item">
                    <div class="cc-snapshot-icon">📈</div>
                    <div>ATS Optimization</div>
                </div>

                <div class="cc-snapshot-item">
                    <div class="cc-snapshot-icon">💼</div>
                    <div>Opportunity Matching</div>
                </div>

                <div class="cc-snapshot-item">
                    <div class="cc-snapshot-icon">🗺️</div>
                    <div>Personalized Roadmap</div>
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        "</div>",
        unsafe_allow_html=True,
    )