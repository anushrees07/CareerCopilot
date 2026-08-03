import streamlit as st


def show():

    st.markdown(
        """
        <div class="stats-section">

            <h2 class="stats-heading">
                Trusted to Accelerate Your Career
            </h2>

            <div class="stats-grid">

                <div class="stat-card">
                    <h1>98%</h1>
                    <p>Resume Match Accuracy</p>
                </div>

                <div class="stat-card">
                    <h1>15K+</h1>
                    <p>Internships Indexed</p>
                </div>

                <div class="stat-card">
                    <h1>5+</h1>
                    <p>AI Providers Supported</p>
                </div>

                <div class="stat-card">
                    <h1>24/7</h1>
                    <p>Career Guidance</p>
                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )