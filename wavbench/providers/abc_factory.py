import torch
from .configs import FWhisperCfg, WhisperCfg, Wav2VecCfg, HFCfg, VoskCfg
from abc import ABC, abstractmethod
from .abc_provider import IaProvider
from typing import Dict, Any

_FASTER_WHISPER: str = "faster_whisper"
_HF: str = "hf"
_WHISPER: str = "whisper"
_WAV2VEC: str = "wav2vec"
_VOSK: str = "vosk"


def _get_param(data: Dict[str, Any], param: str, provider: str) -> Any:
    if param not in data:
        raise KeyError(f"Config data of {provider} missing {param}.")
    return data[param]


class ProviderFactoryABC(ABC):

    @abstractmethod
    def get_provider(self, name: str, cfg: Dict[str, Any]) -> IaProvider:
        raise NotImplementedError("Implement get_provider method.")

    @staticmethod
    def _get_faster_whisper_cfg(name: str, data: Dict[str, Any]) -> FWhisperCfg:
        return FWhisperCfg(
            model=_get_param(data, "model", name),
            compute_type=_get_param(data, "compute_type", name),
            beam_size=_get_param(data, "beam_size", name),
            device=_get_param(data, "device", name)
        )

    @staticmethod
    def _get_hf_config(name: str, data: Dict[str, Any]) -> HFCfg:
        return HFCfg(
            model=_get_param(data, "model", name),
            device=_get_param(data, "device", name),
            compute_type=_get_param(data, "compute_type", name)
        )

    @staticmethod
    def _get_whisper_cfg(name: str, data: Dict[str, Any]) -> WhisperCfg:
        return WhisperCfg(
            model=_get_param(data, "model", name),
            device=_get_param(data, "device", name),
            language=_get_param(data, "language", name),
            fp16=_get_param(data, "fp16", name)
        )

    @staticmethod
    def _get_wav2vec_cfg(name: str, data: Dict[str, Any]) -> Wav2VecCfg:
        return Wav2VecCfg(
            model=_get_param(data, "model", name),
            device=_get_param(data, "device", name),
            compute_type=_convert_str2dtype(
                _get_param(data, "compute_type", name),
            )
        )

    @staticmethod
    def _get_vosk_cfg(name: str, data: Dict[str, Any]) -> VoskCfg:
        return VoskCfg(
            model=_get_param(data, "model", name)
        )


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
