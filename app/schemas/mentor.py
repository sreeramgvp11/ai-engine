# this file helps the defining the request and response for the assistant 

from pydantic import BaseModel
from typing import List


class MentorRequest(BaseModel):
    provider: str
    api_key: str
    model: str
    bug_title: str
    problem_statement: str
    user_message: str
    previous_hints: List[str] = []


class MentorResponse(BaseModel):
    hint: str
    should_reveal_solution: bool = False