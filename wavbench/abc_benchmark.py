import logging
from abc import ABC, abstractmethod
from .providers.abc_transcriber import Transcriber
from typing import Dict

logger: logging.Logger = logging.getLogger(__file__)


class BenchmarkABC(ABC):
    """Interface that defines the operation and control of benchmarks."""

    @property
    @abstractmethod
    def transcribers(self) -> Dict[str, Transcriber]:
        raise NotImplementedError("Implement transcribers property.")

    @abstractmethod
    def run(self) -> str:
        raise NotImplementedError("Implement run method.")

    @abstractmethod
    def run_with_transcriber(self, name: str) -> str:
        raise NotImplementedError("Implement run with transcriber method.")

    def add_provider(self, name: str, transcriber: Transcriber) -> None:
        if not isinstance(transcriber, Transcriber):
            raise ValueError(
                f"Transcriber {name} is not instance of Transcriber.",
            )

        self.transcribers[name] = transcriber

    def remove_provider(self, name: str) -> None:
        if name not in self.transcribers:
            raise KeyError(f"Provider {name} does not exists.")

        self.transcribers.pop(name)
