import streamlit as st


def show(ats_score, skills):

    st.markdown("## 📊 Resume Snapshot")

    st.caption(
        "A quick intelligence report generated from your resume."
    )

    st.write("")

    # ========================================================
    # TOP METRICS
    # ========================================================

    col1, col2, col3, col4 = st.columns(
        4,
        gap="medium",
    )

    with col1:

        with st.container(
            border=True,
            key="resume-stat-ats",
        ):

            st.markdown("### 🎯")

            st.metric(
                "ATS",
                f"{ats_score}%",
            )

            st.caption(
                "Compatibility"
            )

    with col2:

        with st.container(
            border=True,
            key="resume-stat-skills",
        ):

            st.markdown("### 🧠")

            st.metric(
                "Skills",
                len(skills),
            )

            st.caption(
                "Detected"
            )

    with col3:

        with st.container(
            border=True,
            key="resume-stat-grade",
        ):

            st.markdown("### ⭐")

            st.metric(
                "Resume",
                "A+",
            )

            st.caption(
                "Overall grade"
            )

    with col4:

        with st.container(
            border=True,
            key="resume-stat-pages",
        ):

            st.markdown("### 📄")

            st.metric(
                "Pages",
                "1",
            )

            st.caption(
                "Resume length"
            )

    st.write("")

    # ========================================================
    # ATS INSIGHT
    # ========================================================

    with st.container(
        border=True,
        key="resume-score-panel",
    ):

        st.markdown("### 🎯 ATS Compatibility")

        if ats_score >= 80:

            st.success(
                "Excellent ATS compatibility. "
                "Your resume is well optimized for automated screening."
            )

        elif ats_score >= 60:

            st.warning(
                "Good foundation. A few improvements could "
                "make your resume more ATS-friendly."
            )

        else:

            st.error(
                "Your ATS score needs improvement. "
                "Consider strengthening keywords, formatting and role relevance."
            )

        st.progress(
            min(max(ats_score, 0), 100) / 100
        )

    st.write("")

    # ========================================================
    # SKILLS
    # ========================================================

    with st.container(
        border=True,
        key="resume-skills-panel",
    ):

        st.markdown("### 🛠 Skills Detected")

        if not skills:

            st.warning(
                "No skills detected."
            )

            return

        st.caption(
            f"CareerCopilot identified {len(skills)} "
            "skills from your resume."
        )

        st.write("")

        cols = st.columns(3)

        for i, skill in enumerate(skills):

            with cols[i % 3]:

                st.success(
                    skill
                )