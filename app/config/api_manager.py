from app.storage.settings_manager import load_settings


class APIManager:

    @staticmethod
    def get_provider():

        return load_settings()["provider"]

    @staticmethod
    def get_gemini_key():

        return load_settings()["gemini_key"]

    @staticmethod
    def get_openai_key():

        return load_settings()["openai_key"]

    @staticmethod
    def get_claude_key():

        return load_settings()["claude_key"]

    @staticmethod
    def get_openrouter_key():

        return load_settings()["openrouter_key"]