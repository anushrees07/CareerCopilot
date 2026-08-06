from app.models.opportunity import Opportunity


def calculate_match(opportunity, user_skills):

    if not opportunity.skills:
        return 0

    matched = 0

    for skill in opportunity.skills:

        if skill.lower() in [
            s.lower() for s in user_skills
        ]:
            matched += 1

    return int(
        matched / len(opportunity.skills) * 100
    )