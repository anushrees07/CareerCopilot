from app.ai.ai_factory import get_ai_provider


def analyze_resume(resume_text: str):

    provider = get_ai_provider("Gemini")

    return provider.analyze_resume(resume_text)