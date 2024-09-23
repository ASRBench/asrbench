from dataclasses import dataclass
from typing import Dict


@dataclass
class TranscribeResult:
    audio: str
    ia: str
    params: Dict[str, str]
    reference: str
    hypothesis: str
    audio_duration: float
    runtime: float
    rtf: float
    wer: float
    accuracy: float
