from app.storage.settings_manager import load_settings


class APIManager:

    @staticmethod
    def get_provider():

        return load_settings().get(
            "provider",
            "Gemini",
        )

    @staticmethod
    def get_gemini_key():

        return load_settings().get(
            "gemini_key",
            "",
        )

    @staticmethod
    def get_openai_key():

        return load_settings().get(
            "openai_key",
            "",
        )

    @staticmethod
    def get_claude_key():

        return load_settings().get(
            "claude_key",
            "",
        )

    @staticmethod
    def get_openrouter_key():

        return load_settings().get(
            "openrouter_key",
            "",
        )