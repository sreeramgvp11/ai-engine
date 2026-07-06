# this file defines which ai provider that user wants to use 

from pydantic import BaseModel
from typing import Literal


class ProviderConfig(BaseModel):
    provider: Literal["openai", "gemini", "claude"]
    api_key: str
    model: str