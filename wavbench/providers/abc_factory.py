import torch
from .configs import FWhisperCfg, WhisperCfg, Wav2VecCfg
from abc import ABC, abstractmethod
from .abc_provider import IaProvider
from typing import Dict, Any

_FASTER_WHISPER: str = "faster_whisper"
_WHISPER: str = "whisper"
_WAV2VEC: str = "wav2vec"
_VOSK: str = "vosk"


def _get_param(data: Dict[str, Any], param: str, provider: str) -> Any:
    if data[param] is None:
        raise KeyError(f"Config data of {provider} missing {param}.")
    return data[param]


class ProviderFactoryABC(ABC):

    @abstractmethod
    def get_provider(self, name: str, cfg: Dict[str, Any]) -> IaProvider:
        raise NotImplementedError("Implement get_provider method.")

    @staticmethod
    def _get_faster_wisper_cfg(data: Dict[str, Any]) -> FWhisperCfg:
        return FWhisperCfg(
            model_size=_get_param(data, "model_size", _FASTER_WHISPER),
            compute_type=_get_param(data, "compute_type", _FASTER_WHISPER),
            beam_size=_get_param(data, "beam_size", _FASTER_WHISPER),
            device=_get_param(data, "device", _FASTER_WHISPER)
        )

    @staticmethod
    def _get_whisper_cfg(data: Dict[str, Any]) -> WhisperCfg:
        return WhisperCfg(
            model_size=_get_param(data, "model_size", _WHISPER),
            device=_get_param(data, "device", _WHISPER),
            language=_get_param(data, "language", _WHISPER),
            fp16=_get_param(data, "fp16", _WHISPER)
        )

    @staticmethod
    def _get_wav2vec_cfg(data: Dict[str, Any]) -> Wav2VecCfg:
        return Wav2VecCfg(
            checkpoint=_get_param(data, "checkpoint", _WAV2VEC),
            device=_get_param(data, "device", _WAV2VEC),
            compute_type=_convert_str2dtype(
                _get_param(data, "compute_type", _WAV2VEC),
            )
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
