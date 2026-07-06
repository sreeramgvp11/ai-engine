from langchain_anthropic import ChatAnthropic # type: ignore
from app.providers.base import BaseLLMProvider


class ClaudeProvider(BaseLLMProvider):
    def __init__(self, api_key: str, model: str):
        self.llm = ChatAnthropic(
            api_key=api_key,
            model=model,
            temperature=0.2
        )

    def invoke(self, prompt: str) -> str:
        response = self.llm.invoke(prompt)
        return response.content