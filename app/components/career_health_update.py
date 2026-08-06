import streamlit as st


def show(before=72, after=89):

    st.subheader("📈 Career Health")

    col1, col2, col3 = st.columns([1, 0.5, 1])

    with col1:
        st.metric("Before", before)

    with col2:
        st.markdown("## ➜")

    with col3:
        st.metric(
            "After",
            after,
            after - before,
        )