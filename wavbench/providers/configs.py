import torch
from dataclasses import dataclass


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
    device: str
    compute_type: torch.dtype


@dataclass
class HFCfg:
    checkpoint: str
    compute_type: torch.dtype
    device: str


@dataclass
class VoskCfg:
    ...
