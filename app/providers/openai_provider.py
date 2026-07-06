from langchain_openai import ChatOpenAI # type: ignore
from langchain_core.messages import SystemMessage, HumanMessage
from app.providers.base import BaseLLMProvider


class OpenAIProvider(BaseLLMProvider):
    def __init__(self, api_key: str, model: str):
        self.llm = ChatOpenAI(
            api_key=api_key,
            model=model,
            temperature=0.2
        )

    def invoke(self, system_prompt: str,user_prompt:str) -> str:
        response = self.llm.invoke([
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt)
        ])
        return response.content