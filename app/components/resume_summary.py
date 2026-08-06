import streamlit as st


def show(ats_score, skills):

    st.markdown("## 📊 Resume Snapshot")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("🎯 ATS", f"{ats_score}%")
    c2.metric("🧠 Skills", len(skills))
    c3.metric("⭐ Resume", "A+")
    c4.metric("📄 Pages", "1")

    st.divider()

    st.markdown("### 🛠 Skills Detected")

    if not skills:
        st.warning("No skills detected.")
        return

    cols = st.columns(3)

    for i, skill in enumerate(skills):
        with cols[i % 3]:
            st.success(skill)