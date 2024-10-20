import time
import yaml
from pydub import AudioSegment
from pathlib import Path
from typing import Dict, Any
from .providers.factory import ProviderFactory


def check_path(filepath: str) -> None:
    """Check provided path if something wrong raise error."""
    if not filepath:
        raise ValueError("Empty path provided.")

    path = Path(filepath)

    if not path.exists():
        raise FileNotFoundError(f"File {path.name} in {path} does not exists.")


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
        return round(len(audio)/1000, 3)


def read_config_data(filepath_: str) -> Dict[str, Any]:
    """Recover config data from configfile."""
    check_path(filepath_)

    with open(filepath_, "r") as file:
        config: Dict[str, Any] = yaml.safe_load(file)

    return config


def gen_dataset_references(config_path: str) -> None:
    config: Dict[str, Any] = read_config_data(config_path)
    provider_factory = ProviderFactory()

    if "datasets" not in config:
        raise KeyError("Configfile missing datasets.")


def write_file(filepath_: str, data: str) -> None:
    pass
