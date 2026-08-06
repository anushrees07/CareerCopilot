import json
from pathlib import Path

from app.models.opportunity import Opportunity


DATA_FILE = Path("app/data/opportunities.json")


def load_opportunities():

    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    opportunities = []

    for item in data:

        opportunities.append(

            Opportunity(
                title=item["title"],
                company=item["company"],
                location=item["location"],
                type=item["type"],
                skills=item["skills"],
                apply_link=item["apply_link"],
            )

        )

    return opportunities