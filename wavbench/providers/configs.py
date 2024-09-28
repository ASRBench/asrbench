from dataclasses import dataclass
from torch import dtype


@dataclass
class FWhisperCfg:
    model_size: str
    compute_type: str
    device: str
    beam_size: int


@dataclass
class WhisperCfg:
    model_size: str
    device: str
    language: str
    fp16: bool


@dataclass
class Wav2VecCfg:
    checkpoint: str
    compute_type: dtype
    device: str


@dataclass
class HFCfg:
    checkpoint: str
    compute_type: dtype
    device: str


@dataclass
class VoskCfg:
    ...
