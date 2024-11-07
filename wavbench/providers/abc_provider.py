from abc import ABC, abstractmethod
from typing import Dict, Any


class ASRProvider(ABC):
    """Interface to any ASR system."""

    @classmethod
    @abstractmethod
    def from_config(cls, name: str, config: Dict[str, Any]):
        """Create a new ASRProvider from a name and configuration Dict.

        Arguments:
            name: ASR configuration name.
            config: Dict with ASR configuration.
        """
        raise NotImplementedError("Implement from_config method.")

    @property
    @abstractmethod
    def params(self) -> Dict[str, Any]:
        """Parameters passed in the ASR system configuration."""
        raise NotImplementedError("Implement params property.")

    @property
    @abstractmethod
    def name(self) -> str:
        """Name given to the ASR setting in the configuration file."""
        raise NotImplementedError("Implement name property.")

    @abstractmethod
    def transcribe(self, audio_path: str) -> str:
        """Transcribes from the path of the audio file provided."""
        raise NotImplementedError("Implement transcribe method.")

    @abstractmethod
    def load(self) -> None:
        """Loads all the instances needed for ASR to work into memory."""
        raise NotImplementedError("Implement load model method.")

    @abstractmethod
    def unload(self) -> None:
        """Unloads all instances created by ASR from memory."""
        raise NotImplementedError("Implement unload model method.")
