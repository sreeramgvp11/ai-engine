# this is the router manager for the application
from fastapi import APIRouter
from app.api.v1.routes.health import router as health_router
from app.api.v1.routes.generate_bug import router as generate_bug_router
from app.api.v1.routes.mentor import router as mentor_router
from app.api.v1.routes.test_llm import router as test_llm_router
router = APIRouter()

router.include_router(health_router)
router.include_router(generate_bug_router)
router.include_router(mentor_router)
router.include_router(test_llm_router)