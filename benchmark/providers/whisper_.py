from typing import Dict, Any
from abc_provider import IaProvider
import whisper


class Whisper(IaProvider):
    def __init__(self, language, device, model_size: str, fp16: bool):
        self.__lang: str = language
        self.__fp16: bool = fp16
        self.__model = whisper.load_model(
            name=model_size,
            device=device
        )
        self.__params = None

    @property
    def params(self) -> Dict[str, Any]:
        return self.__params

    def transcribe(self, audio_path: str) -> str:
        raise NotImplementedError("Implement transcribe method.")


model = whisper.load_model(
    name="base",
    device="cpu",
)
