import json
from pathlib import Path


SETTINGS_FILE = Path(
    "app/storage/user_settings.json"
)


DEFAULT_SETTINGS = {
    "provider": "Gemini",
    "gemini_key": "",
    "openai_key": "",
    "claude_key": "",
    "openrouter_key": "",
}


def load_settings():

    if not SETTINGS_FILE.exists():

        save_settings(
            DEFAULT_SETTINGS
        )

        return DEFAULT_SETTINGS.copy()

    try:

        with open(
            SETTINGS_FILE,
            "r",
            encoding="utf-8",
        ) as f:

            saved_settings = json.load(f)

    except (
        json.JSONDecodeError,
        OSError,
    ):

        return DEFAULT_SETTINGS.copy()

    settings = DEFAULT_SETTINGS.copy()

    settings.update(
        saved_settings
    )

    return settings


def save_settings(data):

    SETTINGS_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    settings = DEFAULT_SETTINGS.copy()

    settings.update(data)

    with open(
        SETTINGS_FILE,
        "w",
        encoding="utf-8",
    ) as f:

        json.dump(
            settings,
            f,
            indent=4,
        )