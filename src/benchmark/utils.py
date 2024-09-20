from pydub import AudioSegment
from pathlib import Path


def check_path(filepath: str) -> None:
    """Check provided path if something wrong raise error."""
    if not filepath:
        raise ValueError("Empty path provided.")

    path = Path(filepath)

    if not path.exists():
        raise FileNotFoundError("File does not exists.")


def get_rtf(runtime: float, audio_path: str) -> float:
    rtf: float = runtime / __get_audio_duration(audio_path)
    return round(rtf, 2)


def __get_audio_duration(audio_path: str) -> float:
    audio = AudioSegment.from_wav(audio_path)
    if audio is not None:
        return len(audio) / 1000
