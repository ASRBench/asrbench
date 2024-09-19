from dataclasses import dataclass
from faster_whisper.transcribe import TranscriptionInfo


@dataclass
class FasterWhisperCfg:
    ModelSize: str
    Device: str
    Compute_Type: str
    Beam_Size: int
    Audio_Path: str
    Reference: str


@dataclass
class FasterWhisperData:
    Info: TranscriptionInfo
    Wer: float
    Cfg: FasterWhisperCfg
