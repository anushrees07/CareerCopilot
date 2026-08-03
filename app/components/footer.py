import streamlit as st


def show():

    st.markdown(
        """
        <div class="cc-footer">

            <div class="footer-logo">
                🚀 CareerCopilot
            </div>

            <p class="footer-text">
                Build your dream career with AI powered tools.
            </p>

            <p class="footer-copy">
                © 2026 CareerCopilot. Built with ❤️ using Streamlit & AI.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )