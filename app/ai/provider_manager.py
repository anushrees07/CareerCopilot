from app.ai.providers.gemini import GeminiProvider
from app.ai.providers.openrouter import OpenRouterProvider
from app.ai.providers.openai_provider import OpenAIProvider
from app.ai.providers.claude import ClaudeProvider


class ProviderManager:

    def __init__(self):

        self.providers = {
            "Gemini": GeminiProvider,
            "OpenRouter": OpenRouterProvider,
            "OpenAI": OpenAIProvider,
            "Claude": ClaudeProvider
        }

    def get_provider(self, provider_name, api_key):

        provider = self.providers.get(provider_name)

        if provider is None:
            raise ValueError("Unsupported provider")

        return provider(api_key)