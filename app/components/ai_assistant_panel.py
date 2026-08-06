import streamlit as st


SUGGESTIONS = [
    "📝 Review my Resume",
    "🎯 Improve my ATS Score",
    "💼 Find AI Internships",
    "🚀 Generate Career Roadmap",
    "🎤 Start Mock Interview",
    "🧠 Suggest Skills to Learn",
]


def show():

    st.markdown("## 🤖 CareerCopilot AI")

    with st.container(border=True):

        st.markdown("### 👋 Welcome back!")

        st.caption("Your personal AI career mentor.")

        st.write("How can I help you today?")

        st.divider()

        cols = st.columns(2)

        for i, text in enumerate(SUGGESTIONS):

            with cols[i % 2]:
                st.button(
                    text,
                    key=f"ai_{i}",
                    use_container_width=True,
                )

        st.divider()

        prompt = st.text_input(
            "Ask CareerCopilot anything...",
            placeholder="Example: How do I improve my resume for Google?"
        )

        if st.button(
            "🚀 Ask AI",
            use_container_width=True,
        ):

            if not prompt.strip():

                st.warning("Please enter a question.")

            else:

                with st.spinner("CareerCopilot is thinking..."):

                    # Temporary response
                    st.success(
                        "AI integration is coming next! "
                        "This panel will connect to Gemini, OpenAI, Claude and OpenRouter."
                    )