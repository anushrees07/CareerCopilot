import anthropic

from app.ai.providers.base_provider import BaseProvider
from app.config.api_manager import APIManager


class ClaudeProvider(BaseProvider):

    def __init__(self):

        api_key = APIManager.get_claude_key()

        if not api_key:
            raise ValueError(
                "Claude API key not found. "
                "Please configure it in Settings."
            )

        self.client = anthropic.Anthropic(
            api_key=api_key
        )

        self.model = "claude-3-5-haiku-latest"

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

        response = self.client.messages.create(
            model=self.model,
            max_tokens=2000,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.content[0].text

    def chat(self, prompt: str):

        response = self.client.messages.create(
            model=self.model,
            max_tokens=2000,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.content[0].text