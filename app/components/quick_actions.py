import streamlit as st


def navigate(page_name):
    st.session_state.page = page_name
    st.rerun()


def show():

    st.markdown("## ⚡ Quick Actions")

    col1, col2 = st.columns(2)

    with col1:

        with st.container(border=True):

            st.subheader("📄 Resume Analyzer")
            st.caption(
                "Upload your resume and receive AI-powered feedback."
            )

            if st.button(
                "Open Resume Analyzer",
                key="resume_btn",
                use_container_width=True,
            ):
                navigate("📄 Resume Analyzer")

    with col2:

        with st.container(border=True):

            st.subheader("💼 Opportunity Finder")
            st.caption(
                "Find internships, jobs, hackathons and more."
            )

            if st.button(
                "Explore Opportunities",
                key="opp_btn",
                use_container_width=True,
            ):
                navigate("💼 Opportunities")

    st.write("")

    col3, col4 = st.columns(2)

    with col3:

        with st.container(border=True):

            st.subheader("🤖 AI Career Coach")
            st.caption(
                "Ask career questions and get personalized guidance."
            )

            if st.button(
                "Talk to AI",
                key="coach_btn",
                use_container_width=True,
            ):
                navigate("🤖 AI Coach")

    with col4:

        with st.container(border=True):

            st.subheader("🗺 Career Roadmap")
            st.caption(
                "Generate a personalized roadmap for your dream role."
            )

            if st.button(
                "Generate Roadmap",
                key="roadmap_btn",
                use_container_width=True,
            ):
                navigate("🗺 Roadmap")