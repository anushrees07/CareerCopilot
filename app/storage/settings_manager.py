import json
from pathlib import Path

SETTINGS_FILE = Path("app/storage/user_settings.json")


DEFAULT_SETTINGS = {
    "provider": "Gemini",
    "gemini_key": "",
    "openai_key": "",
    "claude_key": "",
    "openrouter_key": "",
}


def load_settings():

    if not SETTINGS_FILE.exists():

        save_settings(DEFAULT_SETTINGS)

        return DEFAULT_SETTINGS

    with open(SETTINGS_FILE, "r") as f:

        return json.load(f)


def save_settings(data):

    SETTINGS_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(SETTINGS_FILE, "w") as f:

        json.dump(data, f, indent=4)