from typing import Dict, Any
from faster_whisper import WhisperModel
from .abc_provider import IaProvider
from .configs import FWhisperCfg


class FasterWhisper(IaProvider):
    def __init__(self, cfg: FWhisperCfg):
        self.__params: Dict[str, Any] = cfg.__dict__
        self.__beam_size: int = cfg.beam_size
        self.__model = WhisperModel(
            model_size_or_path=cfg.model_size,
            compute_type=cfg.compute_type,
            device=cfg.device,
        )

    @property
    def params(self) -> Dict[str, Any]:
        return self.__params

    @property
    def beam_size(self) -> int:
        return self.__beam_size

    @beam_size.setter
    def beam_size(self, beam_size: int) -> None:
        self.__beam_size = beam_size

    def transcribe(self, audio_path: str) -> str:
        segments, info = self.__model.transcribe(
            audio=audio_path,
            beam_size=self.beam_size,
        )

        return " ".join([seg.text for seg in segments])
