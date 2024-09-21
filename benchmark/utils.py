from pydub import AudioSegment
from pathlib import Path


def check_path(filepath: str) -> None:
    """Check provided path if something wrong raise error."""
    if not filepath:
        raise ValueError("Empty path provided.")

    path = Path(filepath)

    if not path.exists():
        raise FileNotFoundError("File does not exists.")


def get_rtf(runtime, duration: float) -> float:
    rtf: float = runtime / duration
    return round(rtf, 3)


def get_audio_duration(audio_path: str) -> float:
    audio = AudioSegment.from_wav(audio_path)
    if audio is not None:
        return round(len(audio), 3)
