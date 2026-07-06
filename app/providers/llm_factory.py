from app.schemas.provider import ProviderConfig
from app.providers.base import BaseLLMProvider
from app.providers.openai_provider import OpenAIProvider
from app.providers.gemini_provider import GeminiProvider
from app.providers.claude_provider import ClaudeProvider


def get_llm_provider(config: ProviderConfig) -> BaseLLMProvider:
    if config.provider == "openai":
        return OpenAIProvider(
            api_key=config.api_key,
            model=config.model
        )

    if config.provider == "gemini":
        return GeminiProvider(
            api_key=config.api_key,
            model=config.model
        )

    if config.provider == "claude":
        return ClaudeProvider(
            api_key=config.api_key,
            model=config.model
        )

    raise ValueError(f"Unsupported provider: {config.provider}")