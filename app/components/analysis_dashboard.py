import streamlit as st


def skill_chip(skill):

    st.markdown(
        f"""
        <span class="skill-pill">{skill}</span>
        """,
        unsafe_allow_html=True,
    )


def missing_chip(skill):

    st.markdown(
        f"""
        <span class="missing-pill">{skill}</span>
        """,
        unsafe_allow_html=True,
    )


def ai_card(title, desc):

    st.markdown(
        f"""
<div class="ai-card">

### {title}

{desc}

</div>
""",
        unsafe_allow_html=True,
    )


def show():

    st.markdown("## 📊 ATS Score")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Overall", "91%", "+12")

    with c2:
        st.metric("Readability", "94%", "+4")

    with c3:
        st.metric("Keyword Match", "88%", "+15")

    st.write("")

    st.markdown("## 🧠 Extracted Skills")

    skills = [
        "Python",
        "SQL",
        "Git",
        "Streamlit",
        "Machine Learning",
        "Pandas",
        "NumPy",
        "GitHub",
    ]

    cols = st.columns(4)

    for i, skill in enumerate(skills):
        with cols[i % 4]:
            skill_chip(skill)

    st.write("")

    st.markdown("## 🎯 Missing Skills")

    missing = [
        "Docker",
        "FastAPI",
        "AWS",
        "Linux",
        "CI/CD",
    ]

    cols = st.columns(3)

    for i, skill in enumerate(missing):
        with cols[i % 3]:
            missing_chip(skill)

    st.write("")

    st.markdown("## 💡 AI Recommendations")

    ai_card(
        "🚀 Improve Projects",
        "Add measurable achievements and GitHub links.",
    )

    ai_card(
        "📈 ATS Optimization",
        "Include keywords matching your target internship.",
    )

    ai_card(
        "💼 Career Advice",
        "Build two more AI projects before internship season.",
    )