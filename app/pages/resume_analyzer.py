import streamlit as st

from app.components.upload_box import show as upload_box
from app.components.analysis_progress import show as analysis_progress

from app.services.resume_parser import extract_text
from app.services.ats_engine import calculate_ats

from app.ai.resume_analyzer import analyze_resume

from app.storage.profile_manager import save_profile


def show():

    st.markdown(
        """
<div class="ai-badge">
✨ Resume Intelligence
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
<div class="section-title">
Analyze Your Resume With AI
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
<div class="section-sub">
Upload your resume to receive an ATS score,
AI feedback, detected skills and career insights.
</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")

    col1, col2 = st.columns([2.3, 1])

    with col1:

        uploaded_file = upload_box()

    with col2:

        with st.container(border=True):

            st.subheader("🚀 Features")

            st.success("ATS Analysis")
            st.success("Skill Detection")
            st.success("AI Feedback")
            st.success("Resume Summary")
            st.success("Career Insights")
            st.success("PDF & DOCX Support")

    st.write("")

    if uploaded_file is None:

        st.info("👆 Upload your resume to begin.")

        return

    st.write("")

    if st.button(
        "🚀 Analyze Resume",
        use_container_width=True,
    ):

        try:

            analysis_progress()

            # -----------------------------
            # Extract Resume Text
            # -----------------------------

            resume_text = extract_text(uploaded_file)

            if not resume_text.strip():
                st.error(
                    "Your resume appears to be empty or text couldn't be extracted."
                )
                return

            # -----------------------------
            # ATS
            # -----------------------------

            ats_score, skills = calculate_ats(
                resume_text
            )

            # -----------------------------
            # AI Feedback
            # -----------------------------

            provider = provider_selector()

            ...

            ai_feedback = analyze_resume(
                resume_text,
                provider,
            )

            # -----------------------------
            # Save Profile
            # -----------------------------

            profile = {

                "resume_name": uploaded_file.name,

                "resume_text": resume_text,

                "skills": skills,

                "ats_score": ats_score,

                "career_health": ats_score,

                "ai_feedback": ai_feedback,

            }

            save_profile(profile)

            st.success(
                f"Analysis completed successfully! Found {len(skills)} skills."
            )

            st.divider()

            # =============================
            # ATS
            # =============================

            st.markdown("## 📊 ATS Score")

            st.metric(
                "Overall ATS Score",
                f"{ats_score}%"
            )

            st.progress(ats_score / 100)

            st.write("")

            # =============================
            # Skills
            # =============================

            st.markdown("## 🧠 Skills Detected")

            if skills:

                cols = st.columns(4)

                for i, skill in enumerate(skills):

                    with cols[i % 4]:

                        st.markdown(
                            f"""
<div class="skill-pill">
{skill}
</div>
""",
                            unsafe_allow_html=True,
                        )

            else:

                st.warning(
                    "No recognizable skills found."
                )

            st.write("")

            # =============================
            # AI Feedback
            # =============================

            st.markdown("## 🤖 AI Feedback")

            st.markdown(
                f"""
<div class="ai-card">
{ai_feedback}
</div>
""",
                unsafe_allow_html=True,
            )

            st.write("")

            # =============================
            # Resume Stats
            # =============================

            c1, c2, c3 = st.columns(3)

            with c1:

                st.metric(
                    "Skills",
                    len(skills),
                )

            with c2:

                st.metric(
                    "Characters",
                    len(resume_text.strip()),
                )

            with c3:

                words = len(
                    resume_text.strip().split()
                )

                st.metric(
                    "Words",
                    words,
                )

        except Exception as e:

            st.error(
                f"❌ Analysis failed.\n\n{e}"
            )
