import streamlit as st

from app.components.upload_box import show as upload_box
from app.components.resume_summary import show as resume_summary
from app.components.career_health_update import show as career_health_update

from app.services.resume_parser import extract_text
from app.services.ats_engine import calculate_ats

from app.ai.resume_analyzer import analyze_resume


def show():

    st.title("📄 Resume Intelligence")
    st.caption(
        "Upload your resume and let CareerCopilot analyze it using AI."
    )

    # ==========================================
    # Upload Resume
    # ==========================================

    uploaded_file = upload_box()

    if uploaded_file is None:
        st.info("👆 Upload a PDF or DOCX resume to begin.")
        return

    st.success(f"✅ Uploaded: {uploaded_file.name}")

    # ==========================================
    # Analysis Progress
    # ==========================================

    progress = st.progress(0)

    status = st.empty()

    steps = [
        "📄 Reading Resume...",
        "🧠 Extracting Skills...",
        "🎯 Calculating ATS Score...",
        "🤖 Generating AI Feedback...",
        "✅ Finalizing Report..."
    ]

    for i, step in enumerate(steps):
        status.info(step)
        progress.progress((i + 1) * 20)

    status.success("Analysis Complete!")

    # ==========================================
    # Parse Resume
    # ==========================================

    try:
        resume_text = extract_text(uploaded_file)

    except Exception as e:
        st.error(f"❌ {e}")
        st.stop()

    ats_score, skills = calculate_ats(resume_text)

    ai_feedback = analyze_resume(resume_text)

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

    # ==========================================
    # Resume Summary
    # ==========================================

    st.divider()

    resume_summary(
        ats_score,
        skills,
    )

    # ==========================================
    # AI Feedback
    # ==========================================

    st.divider()

    st.subheader("🤖 AI Career Feedback")

    st.markdown(ai_feedback)

    # ==========================================
    # Career Health
    # ==========================================

    st.divider()

    career_health_update(
        before=72,
        after=min(72 + len(skills), 100),
    )

    # ==========================================
    # Resume Preview
    # ==========================================

    st.divider()

    with st.expander("📄 View Resume Text"):

        st.text(resume_text[:5000])