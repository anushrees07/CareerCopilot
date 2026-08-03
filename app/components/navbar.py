import streamlit as st


def show():
    st.markdown(
        """
        <div class="cc-navbar">

            <div class="cc-logo">
                🚀 CareerCopilot
            </div>

            <div class="cc-nav-links">
                <span>Dashboard</span>
                <span>Resume</span>
                <span>Internships</span>
                <span>AI Coach</span>
                <span>Settings</span>
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )