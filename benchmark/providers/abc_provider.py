from abc import ABC, abstractmethod


class IaProvider(ABC):

    @abstractmethod
    def transcribe(self, audio_path: str) -> str:
        raise NotImplementedError("Implement transcribe method.")
