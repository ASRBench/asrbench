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
class Wav2vecCfg:
    ...


@dataclass
class VoskCfg:
    ...
