def calculate_match(resume_data, internships):
    """
    Compare resume skills with internship requirements and rank internships.
    """

    resume_skills = {
        skill.lower().strip()
        for skill in resume_data.get("skills", [])
    }

    ranked_jobs = []

    for job in internships:

        required_skills = {
            skill.lower().strip()
            for skill in job.get("skills", [])
        }

        matched = sorted(
            list(required_skills.intersection(resume_skills))
        )

        missing = sorted(
            list(required_skills - resume_skills)
        )

        if len(required_skills) == 0:
            score = 0
        else:
            score = round(
                (len(matched) / len(required_skills)) * 100
            )

        ranked_jobs.append(
            {
                **job,
                "match_score": score,
                "matched_skills": matched,
                "missing_skills": missing
            }
        )

    ranked_jobs.sort(
        key=lambda x: x["match_score"],
        reverse=True
    )

    return ranked_jobs