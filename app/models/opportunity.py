from dataclasses import dataclass


@dataclass
class Opportunity:

    title: str
    company: str
    location: str
    type: str

    skills: list

    apply_link: str