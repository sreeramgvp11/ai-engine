from app.schemas.project import ProjectFile, ProjectScanResult

IMPORTANT_DJANGO_FILES = {
    "views.py",
    "models.py",
    "urls.py",
    "serializers.py",
    "forms.py",
    "settings.py",
    "admin.py",
}


IGNORE_PATTERNS = [
    "__pycache__",
    "migrations/",
    ".venv/",
    "venv/",
    "env/",
    "node_modules/",
    ".git/",
]


MAX_FILE_CHARS = 12000


def should_ignore_file(path: str) -> bool:
    normalized_path = path.replace("\\", "/")

    return any(pattern in normalized_path for pattern in IGNORE_PATTERNS)


def is_important_django_file(path: str) -> bool:
    normalized_path = path.replace("\\", "/")
    file_name = normalized_path.split("/")[-1]

    if should_ignore_file(normalized_path):
        return False

    return file_name in IMPORTANT_DJANGO_FILES


def scan_django_project(files: list[ProjectFile]) -> ProjectScanResult:
    selected_files: list[ProjectFile] = []

    for file in files:
        if is_important_django_file(file.path):
            selected_files.append(
                ProjectFile(
                    path=file.path,
                    content=file.content[:MAX_FILE_CHARS],
                )
            )

    return ProjectScanResult(
        framework="django",
        total_files_received=len(files),
        total_files_selected=len(selected_files),
        selected_files=selected_files,
    )