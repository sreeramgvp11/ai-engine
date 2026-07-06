# defines what a project file looks like

from pydantic import BaseModel
from typing import List


class ProjectFile(BaseModel):
    path: str
    content: str


class ProjectContext(BaseModel):
    framework: str
    files: List[ProjectFile]