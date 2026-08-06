import json
from pathlib import Path

PROFILE_FILE = Path("app/storage/user_profile.json")

DEFAULT_PROFILE = {
    "resume_name": "",
    "resume_text": "",
    "skills": [],
    "ats_score": 0,
    "career_health": 0,
    "ai_feedback": "",
}


def load_profile():

    if not PROFILE_FILE.exists():
        save_profile(DEFAULT_PROFILE)
        return DEFAULT_PROFILE.copy()

    try:
        with open(PROFILE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return DEFAULT_PROFILE.copy()


def save_profile(profile):

    PROFILE_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(PROFILE_FILE, "w", encoding="utf-8") as f:
        json.dump(profile, f, indent=4)


def clear_profile():
    save_profile(DEFAULT_PROFILE)