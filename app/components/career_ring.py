import streamlit as st


def show():

    st.markdown("## 🌟 Career Health Ring")

    score = 91

    st.progress(score / 100)

    c1, c2, c3 = st.columns([1, 2, 1])

    with c2:
        st.metric(
            "Career Health",
            f"{score}/100",
            "Excellent 🚀",
        )

    st.caption(
        "Every improvement in your resume, projects and skills increases this score."
    )