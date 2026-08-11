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


def show():

    st.title("⚙️ AI Settings")

    st.caption(
        "Choose your AI provider and securely configure your API key."
    )

    settings = load_settings()

    # ========================================================
    # PROVIDER
    # ========================================================

    st.subheader("🤖 AI Provider")

    current_provider = settings.get(
        "provider",
        "Gemini",
    )

    if current_provider not in PROVIDERS:
        current_provider = "Gemini"

    provider = st.radio(
        "Choose your AI provider",
        PROVIDERS,
        index=PROVIDERS.index(current_provider),
        horizontal=True,
    )

    st.write("")

    provider_info = {
        "Gemini": "Google Gemini models for fast AI-powered career analysis.",
        "OpenAI": "OpenAI models for resume analysis and career guidance.",
        "Claude": "Anthropic Claude models for detailed career insights.",
        "OpenRouter": "Access multiple AI models through one OpenRouter API.",
    }

    st.info(
        f"💡 {provider_info[provider]}"
    )

    st.divider()

    # ========================================================
    # API KEY
    # ========================================================

    st.subheader("🔑 API Key")

    key_names = {
        "Gemini": "gemini_key",
        "OpenAI": "openai_key",
        "Claude": "claude_key",
        "OpenRouter": "openrouter_key",
    }

    key_labels = {
        "Gemini": "Gemini API Key",
        "OpenAI": "OpenAI API Key",
        "Claude": "Claude API Key",
        "OpenRouter": "OpenRouter API Key",
    }

    key_help = {
        "Gemini": "Enter your Google Gemini API key.",
        "OpenAI": "Enter your OpenAI API key.",
        "Claude": "Enter your Anthropic API key.",
        "OpenRouter": "Enter your OpenRouter API key.",
    }

    selected_key_name = key_names[provider]

    selected_key = st.text_input(
        key_labels[provider],
        value=settings.get(
            selected_key_name,
            "",
        ),
        type="password",
        help=key_help[provider],
        placeholder=f"Paste your {provider} API key here...",
    )

    st.caption(
        "🔒 Your API key is stored locally for this CareerCopilot installation."
    )

    st.write("")

    # ========================================================
    # CURRENT CONFIGURATION
    # ========================================================

    existing_key = settings.get(
        selected_key_name,
        "",
    )

    if existing_key:

        st.success(
            f"✅ {provider} API key is configured."
        )

    else:

        st.warning(
            f"⚠️ No {provider} API key configured yet."
        )

    st.divider()

    # ========================================================
    # SAVE
    # ========================================================

    if st.button(
        "💾 Save AI Configuration",
        use_container_width=True,
        type="primary",
    ):

        updated_settings = settings.copy()

        updated_settings["provider"] = provider
        updated_settings[selected_key_name] = selected_key

        save_settings(
            updated_settings
        )

        st.success(
            f"✅ {provider} selected successfully!"
        )

        st.rerun()