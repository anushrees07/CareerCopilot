import streamlit as st

from app.storage.settings_manager import (
    load_settings,
    save_settings,
)


PROVIDERS = [
    "Gemini",
    "OpenAI",
    "Claude",
    "OpenRouter",
]


PROVIDER_INFO = {
    "Gemini": {
        "icon": "✦",
        "description": "Fast AI for resume analysis and career guidance.",
        "key_name": "gemini_key",
        "key_label": "Gemini API Key",
    },
    "OpenAI": {
        "icon": "◉",
        "description": "Powerful AI for detailed career intelligence.",
        "key_name": "openai_key",
        "key_label": "OpenAI API Key",
    },
    "Claude": {
        "icon": "◇",
        "description": "Thoughtful AI for deep career insights.",
        "key_name": "claude_key",
        "key_label": "Claude API Key",
    },
    "OpenRouter": {
        "icon": "◈",
        "description": "Connect to multiple AI models through one API.",
        "key_name": "openrouter_key",
        "key_label": "OpenRouter API Key",
    },
}


def show():

    settings = load_settings()

    # ========================================================
    # SESSION STATE
    # ========================================================

    if "setup_provider" not in st.session_state:

        current_provider = settings.get(
            "provider",
            "Gemini",
        )

        if current_provider not in PROVIDERS:
            current_provider = "Gemini"

        st.session_state.setup_provider = current_provider

    # ========================================================
    # HEADER
    # ========================================================

    st.write("")

    st.title("🚀 Welcome to CareerCopilot")

    st.caption(
        "Let's connect your AI career brain before you enter your dashboard."
    )

    st.write("")

    st.markdown(
        "## 🧠 Choose Your AI Provider"
    )

    st.caption(
        "Select the AI provider you want CareerCopilot to use."
    )

    st.write("")

    # ========================================================
    # PROVIDER CARDS
    # ========================================================

    columns = st.columns(4)

    for index, provider in enumerate(PROVIDERS):

        info = PROVIDER_INFO[provider]

        with columns[index]:

            selected = (
                st.session_state.setup_provider
                == provider
            )

            with st.container(border=True):

                st.markdown(
                    f"### {info['icon']} {provider}"
                )

                st.caption(
                    info["description"]
                )

                st.write("")

                if selected:

                    st.success(
                        "✓ Selected"
                    )

                else:

                    st.write(
                        "Ready to connect"
                    )

                if st.button(
                    f"Select {provider}",
                    key=f"setup_provider_{provider}",
                    use_container_width=True,
                ):

                    st.session_state.setup_provider = (
                        provider
                    )

                    st.rerun()

    st.write("")
    st.divider()
    st.write("")

    # ========================================================
    # API KEY SECTION
    # ========================================================

    provider = st.session_state.setup_provider

    info = PROVIDER_INFO[provider]

    st.markdown(
        f"## 🔑 Connect {provider}"
    )

    st.caption(
        f"Enter your {provider} API key to activate CareerCopilot's AI features."
    )

    key_name = info["key_name"]

    existing_key = settings.get(
        key_name,
        "",
    )

    api_key = st.text_input(
        info["key_label"],
        value=existing_key,
        type="password",
        placeholder=f"Paste your {provider} API key here...",
        key="setup_api_key",
    )

    st.caption(
        "🔒 Your API key is stored locally on this CareerCopilot installation."
    )

    st.write("")

    # ========================================================
    # CONNECTION STATUS
    # ========================================================

    if existing_key:

        st.success(
            f"✅ {provider} is already configured."
        )

    else:

        st.info(
            f"ℹ️ Connect your {provider} API key to continue."
        )

    st.write("")

    # ========================================================
    # LAUNCH BUTTON
    # ========================================================

    left, center, right = st.columns(
        [1, 2, 1]
    )

    with center:

        if st.button(
            "🚀 Launch CareerCopilot",
            use_container_width=True,
            type="primary",
            key="launch_careercopilot",
        ):

            if not api_key.strip():

                st.error(
                    f"Please enter your {provider} API key first."
                )

                st.stop()

            updated_settings = settings.copy()

            updated_settings["provider"] = provider

            updated_settings[key_name] = (
                api_key.strip()
            )

            save_settings(
                updated_settings
            )

            st.session_state.ai_configured = True

            st.session_state.page = (
                "🏠 Dashboard"
            )

            st.success(
                f"🎉 {provider} connected successfully!"
            )

            st.rerun()

    st.write("")

    st.caption(
        "Your selected AI provider will power Resume Intelligence, "
        "AI Career Coach, Roadmaps, Interview Prep and Skill Gap analysis."
    )