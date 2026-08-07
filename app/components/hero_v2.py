import streamlit as st


def show():

    left, right = st.columns([1.4, 1])

    with left:

        st.markdown(
            """
            <div class="hero-badge">
                ✨ AI Powered Career Platform
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="hero-title">
                Build Your Dream
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="hero-gradient">
                Career
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="hero-title">
                With AI
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.caption(
            """
Analyze your resume, discover internships, identify
skill gaps, prepare for interviews and accelerate
your career using AI.
"""
        )

        c1, c2 = st.columns(2)

        with c1:
            st.button(
                "🚀 Get Started",
                use_container_width=True,
            )

        with c2:
            st.button(
                "▶ Watch Demo",
                use_container_width=True,
            )

    with right:

        with st.container(border=True):

            st.metric(
                "Resume Score",
                "92%",
                "+4%"
            )

            st.metric(
                "Internships",
                "18",
                "+5"
            )

            st.metric(
                "Skill Match",
                "84%",
                "+12%"
            )

            st.metric(
                "Interview Ready",
                "76%",
                "+8%"
            )