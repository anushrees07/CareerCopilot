import json
import fitz
import google.generativeai as genai

from app.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def extract_text(pdf_path):
    """
    Extract text from a PDF.
    """
    text = ""

    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()

    return text.strip()


def analyze_resume(pdf_path):
    """
    Analyze resume using Gemini and return structured JSON.
    """

    resume_text = extract_text(pdf_path)

    if not resume_text:
        raise Exception("No text found in the uploaded resume.")

    prompt = f"""
You are an expert technical recruiter.

Analyze the following resume.

Resume:

{resume_text}

Return ONLY valid JSON.

Use exactly this structure:

{{
    "resume_score": 0,
    "summary": "",
    "skills": [],
    "strengths": [],
    "missing_skills": [],
    "suggestions": [],
    "best_roles": []
}}

Rules:
- resume_score should be an integer from 0 to 100.
- skills must contain only technical skills.
- strengths must be short bullet points.
- missing_skills must contain skills that would improve employability.
- suggestions must contain actionable advice.
- best_roles should contain internship roles.
- Do NOT include markdown.
- Do NOT wrap the JSON in ``` blocks.
"""

    response = model.generate_content(prompt)

    text = response.text.strip()

    try:
        return json.loads(text)

    except Exception:
        # Clean up if Gemini accidentally wraps the JSON
        text = text.replace("```json", "").replace("```", "").strip()
        return json.loads(text)