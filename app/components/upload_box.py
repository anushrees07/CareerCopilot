import streamlit as st


def show():

    st.markdown(
        """
### 📂 Upload Resume
Drag & Drop or browse your resume.

Supported formats:

**PDF • DOCX**
"""
    )

    uploaded = st.file_uploader(
        "",
        type=["pdf", "docx"],
        label_visibility="collapsed",
    )

    if uploaded:

        st.success("✅ Resume uploaded successfully!")

        st.write("")

        st.metric(
            "File Name",
            uploaded.name,
        )

        st.metric(
            "Size",
            f"{round(uploaded.size/1024,1)} KB",
        )

    return uploaded