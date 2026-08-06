import streamlit as st

QUESTIONS = {
    "AI Engineer": [
        (
            "Explain supervised vs unsupervised learning.",
            "Supervised learning uses labelled data while unsupervised learning finds hidden patterns in unlabelled data."
        ),
        (
            "What is overfitting?",
            "A model memorizes the training data instead of learning patterns."
        ),
        (
            "Difference between TensorFlow and PyTorch?",
            "TensorFlow is production-oriented while PyTorch is research-friendly."
        ),
    ],
    "Backend Developer": [
        (
            "What is REST API?",
            "An architectural style for communication using HTTP."
        ),
        (
            "Difference between Flask and FastAPI?",
            "FastAPI is asynchronous and faster while Flask is lightweight and simple."
        ),
    ],
    "Data Scientist": [
        (
            "What is feature engineering?",
            "Creating useful features from raw data."
        ),
        (
            "Difference between Mean and Median?",
            "Median is more robust to outliers."
        ),
    ],
}


def show():

    st.markdown(
        """
<div class="ai-badge">
🎤 Interview Prep
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
<div class="section-title">
Ace Your Next Interview
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
<div class="section-sub">
Practice technical interviews powered by AI.
</div>
""",
        unsafe_allow_html=True,
    )

    role = st.selectbox(
        "Target Role",
        list(QUESTIONS.keys()),
    )

    difficulty = st.selectbox(
        "Difficulty",
        [
            "Beginner",
            "Intermediate",
            "Advanced",
        ],
    )

    st.write("")

    if st.button(
        "🎯 Generate Questions",
        use_container_width=True,
    ):

        st.success("Interview Ready!")

        st.write("")

        for i, (question, answer) in enumerate(QUESTIONS[role], start=1):

            with st.expander(f"Q{i}. {question}"):

                st.markdown("### ✅ Suggested Answer")

                st.info(answer)

        st.divider()

        st.subheader("💡 AI Tips")

        st.success("Use the STAR method.")

        st.success("Keep answers concise.")

        st.success("Explain your projects with measurable impact.")

        st.success("Practice speaking aloud.")