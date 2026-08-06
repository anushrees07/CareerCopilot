from app.services.skill_extractor import extract_skills


def calculate_ats(text):

    skills = extract_skills(text)

    score = min(len(skills) * 5, 100)

    return score, skills