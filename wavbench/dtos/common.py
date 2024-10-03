from dataclasses import dataclass
from typing import Dict


@dataclass
class Measures:
    wer: float
    cer: float
    mer: float
    wil: float
    wip: float


@dataclass
class TranscribeResult:
    audio: str
    ia: str
    params: Dict[str, str]
    reference: str
    hypothesis: str
    measures: Measures
    audio_duration: float
    runtime: float
    rtf: float
    accuracy: float
