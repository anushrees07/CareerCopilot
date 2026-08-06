from abc import ABC, abstractmethod


class BaseProvider(ABC):

    @abstractmethod
    def analyze_resume(self, resume_text: str) -> str:
        pass

    @abstractmethod
    def chat(self, prompt: str) -> str:
        pass