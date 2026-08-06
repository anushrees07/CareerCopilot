import streamlit as st


ROADMAPS = {
    "AI Engineer": [
        "Python",
        "SQL",
        "Machine Learning",
        "Deep Learning",
        "LLMs",
        "GenAI",
        "Docker",
        "AWS",
        "Projects",
    ],
    "Data Scientist": [
        "Python",
        "Statistics",
        "SQL",
        "Pandas",
        "Visualization",
        "Machine Learning",
        "Projects",
    ],
    "Backend Developer": [
        "Python",
        "FastAPI",
        "SQL",
        "Docker",
        "Git",
        "AWS",
        "Projects",
    ],
    "Frontend Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "TypeScript",
        "Projects",
    ],
}


def show():

    st.markdown(
        """
<div class="ai-badge">
🗺 AI Roadmap
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
<div class="section-title">
Build Your Dream Career
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
<div class="section-sub">
Generate a personalized roadmap toward your target role.
</div>
""",
        unsafe_allow_html=True,
    )

    role = st.selectbox(
        "Target Role",
        list(ROADMAPS.keys()),
    )

    st.write("")

    roadmap = ROADMAPS[role]

    for i, step in enumerate(roadmap):

        progress = min((i + 1) * 10, 100)

        st.markdown(f"### 📍 Stage {i+1}")

        st.write(step)

        st.progress(progress / 100)

        st.write("")