import torch
from dataclasses import dataclass


@dataclass
class FWhisperCfg:
    model: str
    compute_type: str
    device: str
    beam_size: int


@dataclass
class WhisperCfg:
    model: str
    device: str
    language: str
    fp16: bool


@dataclass
class Wav2VecCfg:
    model: str
    device: str
    compute_type: torch.dtype


@dataclass
class HFCfg:
    model: str
    compute_type: torch.dtype
    device: str


@dataclass
class VoskCfg:
    ...
