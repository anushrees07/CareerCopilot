import streamlit as st


def show():
    st.markdown(
        """
        <div class="cc-hero">

            <div class="cc-badge">
                ✨ AI Powered Career Platform
            </div>

            <h1 class="cc-title">
                Build Your Dream
                <span>Career</span>
                With AI
            </h1>

            <p class="cc-subtitle">
                Analyze your resume, discover internships, identify skill gaps,
                prepare for interviews, and accelerate your career using your
                favorite AI provider.
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1.2, 1.2, 5])

    with col1:
        st.button("🚀 Analyze Resume", use_container_width=True)

    with col2:
        st.button("💼 Find Internships", use_container_width=True)

    with col1:
        st.button("🚀 Analyze Resume", use_container_width=True)

    with col2:
        st.button("💼 Find Internships", use_container_width=True)