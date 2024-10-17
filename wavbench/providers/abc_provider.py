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

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError("Implement name property.")

    @abstractmethod
    def transcribe(self, audio_path: str) -> str:
        raise NotImplementedError("Implement transcribe method.")

    @abstractmethod
    def load(self) -> None:
        raise NotImplementedError("Implement load model method.")

    @abstractmethod
    def unload(self) -> None:
        raise NotImplementedError("Implement unload model method.")
