from dataclasses import dataclass
from faster_whisper.transcribe import TranscriptionInfo


@dataclass
class FasterWhisperCfg:
    model_size: str
    device: str
    compute_type: str
    beam_size: int


@dataclass
class FasterWhisperData:
    info: TranscriptionInfo
    wer: float
    cfg: FasterWhisperCfg
