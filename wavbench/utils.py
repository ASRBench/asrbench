import time
import yaml
from pydub import AudioSegment
from pathlib import Path
from typing import Dict, Any
from .providers.factory import DefaultProviderFactory


def check_path(filepath: str) -> None:
    """Check provided path if something wrong raise error."""
    if not filepath:
        raise ValueError("Empty path provided.")

    path = Path(filepath)

    if not path.exists():
        raise FileNotFoundError(f"File {path.name} in {path} does not exists.")


def get_filename(filepath_: str) -> str:
    return Path(filepath_).name


def get_runtime(start: float) -> float:
    """Return time since start in seconds."""
    return round(
        (time.time() - start),
        3,
    )


def get_rtf(runtime, duration: float) -> float:
    """Calculate Real Time Factor [RTF] in seconds."""
    rtf: float = runtime / duration
    return round(rtf, 3)


def get_audio_duration(audio_path: str) -> float:
    """Get audio duration in seconds"""
    audio = AudioSegment.from_wav(audio_path)
    if audio is not None:
        return round(len(audio) / 1000, 3)
