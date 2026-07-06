#this endpoint serves to generate bug 
from fastapi import APIRouter
from app.schemas.bug import GenerateBugRequest, GeneratedBugResponse

router = APIRouter(prefix="/generate-bug", tags=["Generate Bug"])


@router.post("/", response_model=GeneratedBugResponse)
async def generate_bug(request: GenerateBugRequest):
    # Temporary mock response.
    # Later this will call LangGraph + LLM provider.
    return GeneratedBugResponse(
        title="Missing Authentication Check",
        difficulty="Medium",
        file_path="accounts/views.py",
        original_code_snippet='def profile(request):\n    return render(request, "profile.html")',
        modified_code_snippet='def profile(request):\n    return render(request, "profile.html")',
        problem_statement="Users are able to access the profile page without being authenticated.",
        expected_behavior="Only logged-in users should be able to access the profile page.",
        actual_behavior="Anonymous users can access the profile page.",
        hints=[
            "Find which view controls the profile route.",
            "Compare this view with another protected view.",
            "Look for missing authentication-related checks."
        ]
    )