import streamlit as st


def show():

    st.markdown("### 🤖 AI Provider")

    providers = [
        "Gemini",
        "OpenRouter",
        "OpenAI",
        "Claude",
    ]

    if "selected_provider" not in st.session_state:
        st.session_state.selected_provider = "Gemini"

    provider = st.selectbox(
        "",
        providers,
        index=providers.index(st.session_state.selected_provider),
        label_visibility="collapsed",
    )

    st.session_state.selected_provider = provider

    st.write("")

    if provider == "Gemini":
        st.success("⚡ Gemini Selected")

    elif provider == "OpenRouter":
        st.info("🌍 OpenRouter Selected")

    elif provider == "OpenAI":
        st.info("🧠 OpenAI Selected")

    else:
        st.info("🤖 Claude Selected")

    return provider