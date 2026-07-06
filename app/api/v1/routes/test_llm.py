from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.schemas.provider import ProviderConfig
from app.providers.llm_factory import get_llm_provider


router = APIRouter(prefix="/test-llm", tags=["Test LLM"])


class TestLLMRequest(BaseModel):
    provider: str
    api_key: str
    model: str
    prompt: str


@router.post("/")
async def test_llm(request: TestLLMRequest):
    try:
        config = ProviderConfig(
            provider=request.provider,
            api_key=request.api_key,
            model=request.model
        )

        llm = get_llm_provider(config)
        response = llm.invoke(request.prompt)

        return {
            "provider": request.provider,
            "model": request.model,
            "response": response
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))