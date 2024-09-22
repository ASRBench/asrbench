from typing import Dict, Any

from .abc_provider import IaProvider


class Vosk(IaProvider):
    def __init__(self):
        self.__params = None

    @property
    def params(self) -> Dict[str, Any]:
        return self.__params

    def transcribe(self, audio_path: str) -> str:
        raise NotImplementedError("Implement transcribe method.")
