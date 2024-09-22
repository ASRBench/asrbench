from abc import ABC, abstractmethod
from typing import Dict, Any


class IaProvider(ABC):

    @property
    @abstractmethod
    def params(self) -> Dict[str, Any]:
        raise NotImplementedError("Implement params property.")

    @abstractmethod
    def transcribe(self, audio_path: str) -> str:
        raise NotImplementedError("Implement transcribe method.")
