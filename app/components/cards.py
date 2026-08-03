import streamlit as st


def show():

    st.markdown("""
    <div class="feature-section">

        <h2 class="section-title">
            Powerful AI Tools
        </h2>

        <p class="section-subtitle">
            Everything you need to build your dream career using AI.
        </p>

        <div class="cards-grid">

            <div class="feature-card">
                <div class="card-icon">📄</div>
                <h3>Resume Analyzer</h3>
                <p>Receive AI-powered feedback and ATS score.</p>
            </div>

            <div class="feature-card">
                <div class="card-icon">🎯</div>
                <h3>Internship Hunter</h3>
                <p>Find internships from multiple platforms instantly.</p>
            </div>

            <div class="feature-card">
                <div class="card-icon">🤖</div>
                <h3>AI Career Coach</h3>
                <p>Personalized career guidance powered by LLMs.</p>
            </div>

            <div class="feature-card">
                <div class="card-icon">📈</div>
                <h3>Skill Gap Analysis</h3>
                <p>Discover missing skills for your dream role.</p>
            </div>

            <div class="feature-card">
                <div class="card-icon">💬</div>
                <h3>Interview Prep</h3>
                <p>Practice with AI-generated interview questions.</p>
            </div>

            <div class="feature-card">
                <div class="card-icon">⚙️</div>
                <h3>Settings</h3>
                <p>Choose your AI provider and personalize everything.</p>
            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)