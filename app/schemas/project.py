from pydantic import BaseModel
from typing import List


class ProjectFile(BaseModel):
    path: str
    content: str


class ProjectScanResult(BaseModel):
    framework: str
    total_files_received: int
    total_files_selected: int
    selected_files: List[ProjectFile]