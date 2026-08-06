import streamlit as st

from app.ai.ai_factory import get_ai_provider


def show():

    st.markdown(
        """
<div class="ai-badge">
🤖 AI Career Coach
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
<div class="section-title">
Your Personal Career Mentor
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
<div class="section-sub">
Ask career questions, interview doubts,
resume advice or roadmap guidance.
</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")

    if "coach_messages" not in st.session_state:
        st.session_state.coach_messages = []

    for message in st.session_state.coach_messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

    prompt = st.chat_input(
        "Ask CareerCopilot anything..."
    )

    if prompt:

        st.session_state.coach_messages.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        with st.chat_message("user"):

            st.markdown(prompt)

        try:

            provider = get_ai_provider(
                st.session_state.get(
                    "selected_provider",
                    "Gemini",
                )
            )

            with st.spinner("Thinking..."):

                response = provider.chat(prompt)

        except Exception as e:

            response = f"Error: {e}"

        st.session_state.coach_messages.append(
            {
                "role": "assistant",
                "content": response,
            }
        )

        with st.chat_message("assistant"):

            st.markdown(response)