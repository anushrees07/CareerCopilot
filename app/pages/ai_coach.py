import streamlit as st

from app.ai.ai_factory import get_ai_provider


SUGGESTIONS = [
    "How can I improve my resume?",
    "What skills should I learn next?",
    "How do I prepare for an AI/ML internship?",
    "Review my career roadmap.",
]


def _send_prompt(prompt: str) -> None:
    st.session_state.coach_prefill = prompt
    st.rerun()


def show() -> None:

    st.title("🤖 AI Career Coach")

    st.caption(
        "Your personal career mentor for resumes, interviews, "
        "skills, internships and career planning."
    )

    if "coach_messages" not in st.session_state:
        st.session_state.coach_messages = []

    st.write("")

    with st.container(
        border=True,
        key="coach_intro",
    ):

        st.subheader(
            "✦ Ask CareerCopilot"
        )

        st.write(
            "Tell me what you're trying to achieve and "
            "I'll help you turn it into your next practical step."
        )

        st.write("")

        columns = st.columns(
            2,
            gap="small",
        )

        for index, prompt in enumerate(SUGGESTIONS):

            with columns[index % 2]:

                if st.button(
                    prompt,
                    key=f"coach_suggestion_{index}",
                    use_container_width=True,
                ):
                    _send_prompt(prompt)

    st.write("")

    for message in st.session_state.coach_messages:

        with st.chat_message(
            message["role"]
        ):
            st.write(
                message["content"]
            )

    prefill = st.session_state.pop(
        "coach_prefill",
        "",
    )

    prompt = st.chat_input(
        "Ask CareerCopilot anything..."
    )

    if prefill and not prompt:
        prompt = prefill

    if not prompt:
        return

    st.session_state.coach_messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):
        st.write(prompt)

    try:

        provider = get_ai_provider()

        with st.chat_message("assistant"):

            with st.spinner(
                "CareerCopilot is thinking..."
            ):
                response = provider.chat(prompt)

            st.write(response)

    except Exception as exc:

        response = (
            "I couldn't reach the configured AI provider "
            "right now.\n\n"
            f"Details: {exc}"
        )

        with st.chat_message("assistant"):
            st.error(response)

    st.session_state.coach_messages.append(
        {
            "role": "assistant",
            "content": response,
        }
    )