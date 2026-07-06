from fastapi import APIRouter
from app.schemas.mentor import MentorRequest, MentorResponse

router = APIRouter(prefix="/mentor", tags=["Mentor"])


@router.post("/", response_model=MentorResponse)
async def mentor(request: MentorRequest):
    # Temporary mock response.
    # Later this will call the AI mentor service.
    return MentorResponse(
        hint="Start by identifying which file contains the route or view related to the failing behavior. Do not jump to code changes yet.",
        should_reveal_solution=False
    )