import streamlit as st


def show():

    st.markdown("### 📤 Upload Your Resume")

    st.caption(
        "Turn your resume into actionable career intelligence."
    )

    st.write("")

    col1, col2 = st.columns(
        2,
        gap="large",
    )

    with col1:

        st.markdown("#### 🔍 What CareerCopilot analyzes")

        st.write("")

        st.markdown("✅ ATS Compatibility")
        st.markdown("✅ AI Resume Review")
        st.markdown("✅ Skill Detection")
        st.markdown("✅ Career Health")

    with col2:

        st.markdown("#### 📄 Supported Formats")

        st.write("")

        st.markdown("📕 **PDF**")

        st.caption(
            "Best for preserving resume formatting."
        )

        st.markdown("📘 **DOCX**")

        st.caption(
            "Great for editable resumes."
        )

    st.write("")

    uploaded = st.file_uploader(
        "Choose Resume",
        type=["pdf", "docx"],
        help="Supported formats: PDF, DOCX",
        key="resume_file_uploader",
    )

    st.caption(
        "🔒 Your resume is used only for CareerCopilot analysis."
    )

    return uploaded