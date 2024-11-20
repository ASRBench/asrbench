from asrbench.transcribers.abc_transcriber import Transcriber
from asrbench.transcribers.registry import register_transcriber
from typing import Dict, Any


@register_transcriber("custom")
class CustomTranscriber(Transcriber):
    def __init__(self, name: str) -> None:
        self._name: str = name
        self.__params: Dict[str, Any] = {}

    @classmethod
    def from_config(cls, name: str, config: Dict[str, Any]):
        pass

    @property
    def params(self) -> Dict[str, Any]:
        return self.__params

    @property
    def name(self) -> str:
        return self._name

    def transcribe(self, audio_path: str) -> str:
        pass

    def load(self) -> None:
        pass

    def unload(self) -> None:
        pass
