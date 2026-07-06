from abc import ABC, abstractmethod


class BaseLLMProvider(ABC):
    @abstractmethod
    def invoke(self, system_prompt: str, user_prompt: str) -> str:
        pass