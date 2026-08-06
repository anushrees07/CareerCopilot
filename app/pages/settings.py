import streamlit as st

from app.storage.settings_manager import (
    load_settings,
    save_settings,
)


def show():

    st.title("⚙ Settings")

    st.caption(
        "Configure your AI providers."
    )

    settings = load_settings()

    st.subheader("🤖 AI Provider")

    provider = st.radio(

        "Choose Provider",

        [

            "Gemini",

            "OpenAI",

            "Claude",

            "OpenRouter",

        ],

        index=[

            "Gemini",

            "OpenAI",

            "Claude",

            "OpenRouter",

        ].index(settings["provider"]),

    )

    st.divider()

    st.subheader("🔑 API Keys")

    gemini = st.text_input(

        "Gemini API Key",

        value=settings["gemini_key"],

        type="password",

    )

    openai = st.text_input(

        "OpenAI API Key",

        value=settings["openai_key"],

        type="password",

    )

    claude = st.text_input(

        "Claude API Key",

        value=settings["claude_key"],

        type="password",

    )

    openrouter = st.text_input(

        "OpenRouter API Key",

        value=settings["openrouter_key"],

        type="password",

    )

    st.divider()

    if st.button(

        "💾 Save Settings",

        use_container_width=True,

    ):

        save_settings(

            {

                "provider": provider,

                "gemini_key": gemini,

                "openai_key": openai,

                "claude_key": claude,

                "openrouter_key": openrouter,

            }

        )

        st.success("Settings saved successfully!")