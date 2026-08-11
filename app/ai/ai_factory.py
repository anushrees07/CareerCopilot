from app.ai.providers.gemini_provider import GeminiProvider
from app.ai.providers.openai_provider import OpenAIProvider
from app.ai.providers.claude_provider import ClaudeProvider
from app.ai.providers.openrouter_provider import OpenRouterProvider

from app.config.api_manager import APIManager


def get_ai_provider():

    provider = APIManager.get_provider()

    providers = {
        "Gemini": GeminiProvider,
        "OpenAI": OpenAIProvider,
        "Claude": ClaudeProvider,
        "OpenRouter": OpenRouterProvider,
    }

    if provider not in providers:

        raise ValueError(
            f"Unsupported AI provider: {provider}"
        )

    return providers[provider]()