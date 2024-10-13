from typing import Dict, Any
from .abc_provider import IaProvider
from .configs import WhisperCfg
import whisper


class Whisper(IaProvider):

    def __init__(self, cfg: WhisperCfg):
        self.__name: str = cfg.name
        self.__lang: str = cfg.language
        self.__fp16: bool = cfg.fp16
        self.__model = whisper.load_model(
            name=cfg.model,
            device=cfg.device
        )
        self.__params = cfg.__dict__

    @property
    def name(self) -> str:
        return self.__name

    @classmethod
    def from_config(cls, name: str, data: Dict[str, Any]):
        return Whisper(WhisperCfg.load(data, name))

    @property
    def params(self) -> Dict[str, Any]:
        return self.__params

    def transcribe(self, audio_path: str) -> str:
        result: Dict[str, Any] = self.__model.transcribe(
            audio=audio_path,
            language=self.__lang,
            fp16=self.__fp16
        )

        return result["text"]
