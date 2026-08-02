from app.ai.providers.gemini import GeminiProvider
from app.ai.providers.openai_provider import OpenAIProvider
from app.ai.providers.claude import ClaudeProvider
from app.ai.providers.openrouter import OpenRouterProvider


class AIGateway:

    @staticmethod
    def get_provider(provider, api_key):

        providers = {

            "Gemini": GeminiProvider,

            "OpenAI": OpenAIProvider,

            "Claude": ClaudeProvider,

            "OpenRouter": OpenRouterProvider

        }

        provider_class = providers.get(provider)

        if provider_class is None:
            raise ValueError("Unsupported AI Provider")

        return provider_class(api_key)