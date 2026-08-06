from app.ai.providers.gemini_provider import GeminiProvider
from app.config.api_manager import APIManager


def get_ai_provider():

    provider = APIManager.get_provider()

    providers = {
        "Gemini": GeminiProvider,
    }

    if provider not in providers:
        raise ValueError(f"{provider} is not implemented yet.")

    return providers[provider]()