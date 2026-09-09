import streamlit as st


QUESTIONS = {
    "AI Engineer": [
        (
            "Explain supervised vs unsupervised learning.",
            "Supervised learning uses labelled data while "
            "unsupervised learning discovers patterns in "
            "unlabelled data.",
        ),
        (
            "What is overfitting?",
            "Overfitting happens when a model learns the "
            "training data too closely and performs poorly "
            "on unseen data.",
        ),
        (
            "Difference between TensorFlow and PyTorch?",
            "Both are deep-learning frameworks. PyTorch is "
            "popular for research and experimentation, while "
            "TensorFlow has strong production tooling.",
        ),
    ],

    "Backend Developer": [
        (
            "What is REST API?",
            "REST is an architectural approach for designing "
            "networked services around resources and HTTP.",
        ),
        (
            "Difference between Flask and FastAPI?",
            "Flask is lightweight and flexible. FastAPI provides "
            "modern type hints, validation and strong async support.",
        ),
    ],

    "Data Scientist": [
        (
            "What is feature engineering?",
            "Feature engineering means transforming raw data "
            "into useful inputs for machine-learning models.",
        ),
        (
            "Difference between Mean and Median?",
            "The mean is the arithmetic average. The median is "
            "the middle value and is generally more resistant "
            "to extreme outliers.",
        ),
    ],
}


def show() -> None:

    st.title("🎤 Interview Prep")

    st.caption(
        "Practice technical interviews with structured "
        "questions, explanations and preparation tips."
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

    if not st.button(
        f"🎯 Generate {difficulty} Questions",
        use_container_width=True,
        type="primary",
    ):
        return

    st.success(
        "Interview session ready!"
    )

    st.write("")

    questions = QUESTIONS[role]

    for index, (
        question,
        answer,
    ) in enumerate(
        questions,
        start=1,
    ):

        with st.container(
            border=True,
            key=f"interview_question_{index}",
        ):

            st.subheader(
                f"Q{index}. {question}"
            )

            st.caption(
                f"Difficulty • {difficulty}"
            )

            with st.expander(
                "Reveal suggested answer"
            ):

                st.write(
                    answer
                )

    st.write("")

    st.subheader(
        "💡 AI Interview Tips"
    )

    tips = [
        "Use the STAR method for behavioral questions.",
        "Keep technical answers concise, then expand when asked.",
        "Explain your projects with measurable impact.",
        "Practice speaking aloud instead of only reading answers.",
    ]

    for tip in tips:
        st.info(tip)