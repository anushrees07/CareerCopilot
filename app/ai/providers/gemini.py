from .base import AIProvider


class GeminiProvider(AIProvider):

    def __init__(self, api_key):

        self.api_key = api_key

    def validate_api_key(self):

        """
        We will implement this later.
        """

        return True

    def analyze_resume(self, resume_text):

        """
        Gemini implementation comes next.
        """

        pass