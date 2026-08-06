from app.storage.profile_manager import load_profile


def calculate_match(job_skills, user_skills):

    if not job_skills:
        return 0

    matched = 0

    for skill in job_skills:

        if skill.lower() in [s.lower() for s in user_skills]:
            matched += 1

    return round((matched / len(job_skills)) * 100)


def rank_opportunities(opportunities):

    profile = load_profile()

    user_skills = profile.get("skills", [])

    ranked = []

    for job in opportunities:

        score = calculate_match(
            job["skills"],
            user_skills,
        )

        job["match"] = score

        ranked.append(job)

    ranked.sort(
        key=lambda x: x["match"],
        reverse=True,
    )

    return ranked