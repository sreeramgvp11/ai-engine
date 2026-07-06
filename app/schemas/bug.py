# this defines the shape of the bug response ; this is very important ; this 

from pydantic import BaseModel
from typing import List


class GenerateBugRequest(BaseModel):
    provider: str
    api_key: str
    model: str
    framework: str
    files: list[dict]


class GeneratedBugResponse(BaseModel):
    title: str
    difficulty: str
    file_path: str
    original_code_snippet: str
    modified_code_snippet: str
    problem_statement: str
    expected_behavior: str
    actual_behavior: str
    hints: List[str]