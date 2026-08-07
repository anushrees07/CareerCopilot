import streamlit as st


def show():

    st.markdown("## 📄 Upload Resume")

    with st.container(border=True):

        st.markdown("### 🚀 Resume Intelligence")

        st.write(
            """
Upload your resume to unlock:

✅ ATS Analysis

✅ AI Resume Review

✅ Skill Detection

✅ Career Health Update
"""
        )

        uploaded = st.file_uploader(
            "Choose Resume",
            type=["pdf", "docx"],
            help="Supported formats: PDF, DOCX",
        )

    return uploaded