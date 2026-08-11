import streamlit as st

from app.components.upload_box import show as upload_box
from app.components.resume_summary import show as resume_summary
from app.components.career_health_update import show as career_health_update

from app.services.resume_parser import extract_text
from app.services.ats_engine import calculate_ats

from app.ai.resume_analyzer import analyze_resume


def show():

    # ========================================================
    # PAGE HEADER
    # ========================================================

    st.title("📄 Resume Intelligence")

    st.caption(
        "Upload your resume and let CareerCopilot analyze it using AI."
    )

    st.write("")

    # ========================================================
    # UPLOAD RESUME
    # ========================================================

    with st.container(
        border=True,
        key="resume-uploader-card",
    ):

        uploaded_file = upload_box()

    # ========================================================
    # STOP UNTIL RESUME IS UPLOADED
    # ========================================================

    if uploaded_file is None:

        st.info(
            "👆 Upload a PDF or DOCX resume to begin."
        )

        return

    # ========================================================
    # UPLOAD SUCCESS
    # ========================================================

    st.success(
        f"✅ Uploaded: {uploaded_file.name}"
    )

    st.write("")

    # ========================================================
    # ANALYSIS PROGRESS
    # ========================================================

    with st.container(
        border=True,
        key="resume-analysis-panel",
    ):

        st.markdown(
            "### 🧠 Resume Analysis"
        )

        progress = st.progress(0)

        status = st.empty()

        steps = [
            "📄 Reading Resume...",
            "🧠 Extracting Skills...",
            "🎯 Calculating ATS Score...",
            "🤖 Generating AI Feedback...",
            "✅ Finalizing Report...",
        ]

        for i, step in enumerate(steps):

            status.info(step)

            progress.progress(
                (i + 1) * 20
            )

        status.success(
            "Analysis Complete!"
        )

    # ========================================================
    # PARSE RESUME
    # ========================================================

    try:

        resume_text = extract_text(
            uploaded_file
        )

    except Exception as e:

        st.error(
            f"❌ {e}"
        )

        st.stop()

    # ========================================================
    # ATS ANALYSIS
    # ========================================================

    ats_score, skills = calculate_ats(
        resume_text
    )

    # ========================================================
    # AI ANALYSIS
    # ========================================================

    ai_feedback = analyze_resume(
        resume_text
    )

    # ========================================================
    # SAVE PROFILE
    # ========================================================

    from app.storage.profile_manager import save_profile

    career_health = min(
        ats_score + len(skills),
        100,
    )

    save_profile(
        {
            "resume_name": uploaded_file.name,
            "resume_text": resume_text,
            "skills": skills,
            "ats_score": ats_score,
            "career_health": career_health,
            "ai_feedback": ai_feedback,
        }
    )

    # ========================================================
    # RESUME SUMMARY
    # ========================================================

    st.write("")

    with st.container(
        border=True,
        key="resume-summary-panel",
    ):

        resume_summary(
            ats_score,
            skills,
        )

    # ========================================================
    # AI FEEDBACK
    # ========================================================

    st.write("")

    with st.container(
        border=True,
        key="resume-ai-feedback",
    ):

        st.markdown(
            "### 🤖 AI Career Feedback"
        )

        st.markdown(
            ai_feedback
        )

    # ========================================================
    # CAREER HEALTH
    # ========================================================

    st.write("")

    with st.container(
        border=True,
        key="resume-health-panel",
    ):

        st.markdown(
            "### 💚 Career Health"
        )

        career_health_update(
            before=72,
            after=min(
                72 + len(skills),
                100,
            ),
        )

    # ========================================================
    # RESUME PREVIEW
    # ========================================================

    st.write("")

    with st.container(
        border=True,
        key="resume-preview-panel",
    ):

        st.markdown(
            "### 📄 Resume Preview"
        )

        with st.expander(
            "View Resume Text"
        ):

            st.text(
                resume_text[:5000]
            )