import re


SKILLS = [
    "Python",
    "Java",
    "C",
    "C++",
    "SQL",
    "Machine Learning",
    "Deep Learning",
    "TensorFlow",
    "PyTorch",
    "Pandas",
    "NumPy",
    "Flask",
    "FastAPI",
    "Django",
    "Git",
    "GitHub",
    "Docker",
    "Kubernetes",
    "Linux",
    "AWS",
    "Azure",
    "GCP",
    "HTML",
    "CSS",
    "JavaScript",
    "React",
]


def extract_skills(text):

    found = []

    text = text.lower()

    for skill in SKILLS:

        if re.search(r"\b" + re.escape(skill.lower()) + r"\b", text):

            found.append(skill)

    return sorted(list(set(found)))