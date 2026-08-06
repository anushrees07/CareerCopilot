import time
import streamlit as st


def show():

    steps = [
        "📄 Reading resume...",
        "🧠 Extracting skills...",
        "📊 Calculating ATS score...",
        "🤖 Asking AI...",
        "✨ Preparing insights..."
    ]

    progress = st.progress(0)

    status = st.empty()

    for i, step in enumerate(steps):

        status.info(step)

        progress.progress((i + 1) / len(steps))

        time.sleep(0.6)

    status.success("✅ Analysis Completed!")