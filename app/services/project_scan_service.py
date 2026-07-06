from app.schemas.project import ProjectFile, ProjectScanResult
from app.scanners.django_scanner import scan_django_project

def scan_project(framework: str, files: list[ProjectFile]) -> ProjectScanResult:
    framework = framework.lower().strip()

    if framework == "django":
        return scan_django_project(files)

    raise ValueError(f"Unsupported framework: {framework}")