from openai import OpenAI

from app.ai.providers.base_provider import BaseProvider
from app.config.api_manager import APIManager


class OpenAIProvider(BaseProvider):

    def __init__(self):

        api_key = APIManager.get_openai_key()

        if not api_key:
            raise ValueError(
                "OpenAI API key not found. "
                "Please configure it in Settings."
            )

        self.client = OpenAI(
            api_key=api_key
        )

        self.model = "gpt-4o-mini"

    def analyze_resume(self, resume_text: str):

        prompt = f"""
You are an expert ATS Resume Reviewer and Career Coach.

Analyze the following resume.

Return your response in Markdown.

Include:

# ATS Score (/100)

# Strengths

# Weaknesses

# Missing Skills

# Resume Improvements

# Final Verdict

Resume:

{resume_text}
"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.choices[0].message.content

    def chat(self, prompt: str):

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.choices[0].message.content