from pathlib import Path


BASE_PROMPT_PATH = Path("app/prompts")


def load_prompt(relative_path: str) -> str:
    path = BASE_PROMPT_PATH / relative_path

    if not path.exists():
        raise FileNotFoundError(f"Prompt file not found: {path}")

    return path.read_text(encoding="utf-8")