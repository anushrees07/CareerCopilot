import streamlit as st
from datetime import datetime


def show():

    year = datetime.now().year

    st.write("")
    st.divider()

    left, center, right = st.columns([2, 2, 1])

    with left:

        st.markdown(
            """
### 🚀 CareerCopilot

Build your dream career using Artificial Intelligence.
"""
        )

    with center:

        st.markdown(
            """
### Quick Links

🏠 Dashboard

📄 Resume Analyzer

💼 Opportunities

🤖 AI Coach
"""
        )

    with right:

        st.markdown(
            f"""
### Version

v1.0.0

© {year}
"""
        )

    st.caption(
        "Made with ❤️ using Streamlit • Gemini • OpenAI • Claude • OpenRouter"
    )