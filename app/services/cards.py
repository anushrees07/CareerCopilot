import os
import tempfile

import streamlit as st

from app.ai.resume_analyzer import analyze_resume
from app.jobs.jobs import get_jobs
from app.utils.matcher import calculate_match

st.set_page_config(
    page_title="CareerCopilot",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 CareerCopilot")

st.caption("Your AI-powered Career Companion")

st.divider()

uploaded_file = st.file_uploader(
    "Upload your Resume",
    type=["pdf"]
)

if uploaded_file is not None:

    if st.button("Analyze Resume"):

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as tmp:

            tmp.write(uploaded_file.getbuffer())

            resume_path = tmp.name

        with st.spinner("Analyzing Resume..."):

            resume_data = analyze_resume(resume_path)

        os.remove(resume_path)

        st.success("Resume analyzed successfully!")

        st.divider()

        st.subheader("Resume Score")

        st.progress(
            resume_data["resume_score"] / 100
        )

        st.metric(
            "Score",
            f'{resume_data["resume_score"]}/100'
        )