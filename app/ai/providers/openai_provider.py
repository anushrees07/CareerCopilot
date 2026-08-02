from .base import AIProvider


class OpenAIProvider(AIProvider):

    def __init__(self, api_key):

        self.api_key = api_key

    def validate_api_key(self):

        return True

    def analyze_resume(self, resume_text):

        pass