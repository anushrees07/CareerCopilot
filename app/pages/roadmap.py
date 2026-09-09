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
        "HTML fundamentals",
        "CSS fundamentals",
        "JavaScript",
        "React",
        "TypeScript",
        "Projects",
    ],
}


def show() -> None:

    st.title("🗺️ AI Career Roadmap")

    st.caption(
        "Build a practical path from your current skills "
        "to your target role."
    )

    role = st.selectbox(
        "Target Role",
        list(ROADMAPS.keys()),
    )

    roadmap = ROADMAPS[role]

    st.write("")

    st.subheader(
        f"🚀 {role} Path"
    )

    total = len(roadmap)

    for index, step in enumerate(
        roadmap,
        start=1,
    ):

        progress = index / total

        with st.container(
            border=True,
            key=f"roadmap_stage_{index}",
        ):

            left, right = st.columns(
                [4, 1],
                gap="small",
            )

            with left:
                st.subheader(
                    f"{index:02d}  {step}"
                )

            with right:
                st.caption(
                    f"{int(progress * 100)}%"
                )

            st.progress(
                progress
            )