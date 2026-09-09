from pathlib import Path


FORBIDDEN = (
    "unsafe_" + "allow_html",
    "<" + "div",
    "<" + "/div",
    "<" + "span",
    "<" + "/span",
    "<" + "style",
    "<" + "/style",
    "<" + "button",
    "<" + "/button",
    "<" + "script",
    "<" + "/script",
    "<" + "img",
    "<" + "/img",
)


def main() -> int:

    root = (
        Path(__file__)
        .resolve()
        .parents[1]
    )

    failures = []

    for path in root.rglob("*.py"):

        if any(
            part in {
                ".git",
                ".venv",
                "venv",
                "__pycache__",
            }
            for part in path.parts
        ):
            continue

        text = path.read_text(
            encoding="utf-8",
            errors="ignore",
        )

        for token in FORBIDDEN:

            if token in text:
                failures.append(
                    (
                        path.relative_to(root),
                        token,
                    )
                )

    if failures:

        print(
            "HTML guard failed:"
        )

        for path, token in failures:
            print(
                f"  {path}: {token}"
            )

        return 1

    print(
        "HTML guard passed. "
        "No HTML UI markup detected "
        "in Python files."
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())