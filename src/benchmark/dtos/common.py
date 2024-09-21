from dataclasses import dataclass


@dataclass
class TranscribeResult:
    ia: str
    model_size: str
    compute_type: str
    beam_size: int
    reference: str
    hypothesis: str
    audio_duration: float
    runtime: float
    rtf: float
    wer: float
    accuracy: float
