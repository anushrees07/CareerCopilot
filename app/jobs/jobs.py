import json
from pathlib import Path


DATA_FILE = Path("data") / "internships.json"


def get_jobs():
    """
    Load internship data.

    In future versions this function can be
    replaced with an API without changing
    the UI.
    """

    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        jobs = json.load(file)

    return jobs