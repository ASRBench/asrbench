from abc import ABC, abstractmethod
from typing import Dict, Any


class IaProvider(ABC):
    @classmethod
    @abstractmethod
    def from_config(cls, name: str, data: Dict[str, Any]):
        raise NotImplementedError("Implement from_config method.")

    @property
    @abstractmethod
    def params(self) -> Dict[str, Any]:
        raise NotImplementedError("Implement params property.")

    @abstractmethod
    def transcribe(self, audio_path: str) -> str:
        raise NotImplementedError("Implement transcribe method.")
