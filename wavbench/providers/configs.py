import torch
from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class FWhisperCfg:
    model: str
    compute_type: str
    device: str
    beam_size: int

    @classmethod
    def load(cls, data: Dict[str, Any], name: str):
        return FWhisperCfg(
            model=_get_config_param(data, "model", name),
            compute_type=_get_config_param(data, "compute_type", name),
            beam_size=_get_config_param(data, "beam_size", name),
            device=_get_config_param(data, "device", name)
        )


@dataclass
class WhisperCfg:
    model: str
    device: str
    language: str
    fp16: bool

    @classmethod
    def load(cls, data: Dict[str, Any], name: str):
        return WhisperCfg(
            model=_get_config_param(data, "model", name),
            device=_get_config_param(data, "device", name),
            language=_get_config_param(data, "language", name),
            fp16=_get_config_param(data, "fp16", name)
        )


@dataclass
class Wav2VecCfg:
    model: str
    device: str
    compute_type: torch.dtype

    @classmethod
    def load(cls, data: Dict[str, Any], name: str):
        return Wav2VecCfg(
            model=_get_config_param(data, "model", name),
            device=_get_config_param(data, "device", name),
            compute_type=_convert_str2dtype(
                _get_config_param(data, "compute_type", name),
            )
        )


@dataclass
class HFCfg:
    model: str
    compute_type: torch.dtype
    device: str

    @classmethod
    def load(cls, data: Dict[str, Any], name: str):
        return HFCfg(
            model=_get_config_param(data, "model", name),
            device=_get_config_param(data, "device", name),
            compute_type=_get_config_param(data, "compute_type", name)
        )


@dataclass
class VoskCfg:
    model: str
    lang: str = "pt"

    @classmethod
    def load(cls, data: Dict[str, Any], name: str):
        return VoskCfg(
            model=_get_config_param(data, "model", name),
            lang=_get_config_param(data, "language", name)
        )


def _get_config_param(data: Dict[str, Any], param: str, provider: str) -> Any:
    if param not in data or data[param] is None:
        raise KeyError(f"Config data of {provider} missing {param}.")
    return data[param]


def _convert_str2dtype(dtype_: str) -> torch.dtype:
    match dtype_:
        case "float64":
            return torch.float64
        case "float32":
            return torch.float32
        case "float16":
            return torch.float16
        case "int64":
            return torch.int64
        case "int32":
            return torch.int32
        case "int16":
            return torch.int16
        case "int8":
            return torch.int8
        case _:
            raise ValueError(f"Torch dtype {dtype_} does not support.")
