import google.generativeai as genai

from app.ai.providers.base_provider import BaseProvider
from app.config.api_manager import APIManager


class GeminiProvider(BaseProvider):

    def __init__(self):

        api_key = APIManager.get_gemini_key()

        if not api_key:
            raise ValueError(
                "Gemini API Key not found. Please add GEMINI_API_KEY to your .env file."
            )

        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    def analyze_resume(self, resume_text: str) -> str:

        prompt = f"""
You are an expert ATS Resume Reviewer and Career Coach.

Analyze the following resume professionally.

Return your response in Markdown.

Include:

# ATS Score (/100)

# Strengths

# Weaknesses

# Missing Skills

# Suggested Improvements

# Final Verdict

Resume:

{resume_text}
"""

        response = self.model.generate_content(prompt)

        return response.text

    def chat(self, prompt: str) -> str:

        response = self.model.generate_content(prompt)

        return response.text