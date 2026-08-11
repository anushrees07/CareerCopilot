import streamlit as st


def navigate(page_name):
    st.session_state.page = page_name
    st.rerun()


def show():

    st.markdown("## ⚡ Quick Actions")

    st.caption(
        "Jump directly into the tools that move your career forward."
    )

    st.write("")

    # ========================================================
    # ROW 1
    # ========================================================

    col1, col2 = st.columns(
        2,
        gap="medium",
    )

    with col1:

        with st.container(
            border=True,
            key="quick-resume",
        ):

            st.markdown("### 📄 Resume Analyzer")

            st.caption(
                "Upload your resume and receive "
                "AI-powered feedback."
            )

            st.write("")

            if st.button(
                "Open Resume Analyzer →",
                key="resume_btn",
                use_container_width=True,
            ):
                navigate("📄 Resume Analyzer")

    with col2:

        with st.container(
            border=True,
            key="quick-opportunities",
        ):

            st.markdown("### 💼 Opportunity Finder")

            st.caption(
                "Find internships, jobs, hackathons "
                "and more."
            )

            st.write("")

            if st.button(
                "Explore Opportunities →",
                key="opp_btn",
                use_container_width=True,
            ):
                navigate("💼 Opportunities")

    # ========================================================
    # ROW 2
    # ========================================================

    st.write("")

    col3, col4 = st.columns(
        2,
        gap="medium",
    )

    with col3:

        with st.container(
            border=True,
            key="quick-coach",
        ):

            st.markdown("### 🤖 AI Career Coach")

            st.caption(
                "Ask career questions and get "
                "personalized guidance."
            )

            st.write("")

            if st.button(
                "Talk to AI →",
                key="coach_btn",
                use_container_width=True,
            ):
                navigate("🤖 AI Coach")

    with col4:

        with st.container(
            border=True,
            key="quick-roadmap",
        ):

            st.markdown("### 🗺️ Career Roadmap")

            st.caption(
                "Generate a personalized roadmap "
                "for your dream role."
            )

            st.write("")

            if st.button(
                "Generate Roadmap →",
                key="roadmap_btn",
                use_container_width=True,
            ):
                navigate("🗺 Roadmap")