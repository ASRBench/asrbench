from pathlib import Path


def check_path(filepath: str) -> None:
    """Check provided path if something wrong raise error."""
    if not filepath:
        raise ValueError("Empty path provided.")

    path = Path(filepath)

    if not path.exists():
        raise FileNotFoundError("File does not exists.")
