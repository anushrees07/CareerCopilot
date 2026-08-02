from abc import ABC, abstractmethod


class AIProvider(ABC):

    def __init__(self, api_key):

        self.api_key = api_key

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def analyze_resume(self, resume_text):
        pass