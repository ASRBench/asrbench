import logging
import time
import benchmark.utils as utils
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path
from .providers.abc_provider import IaProvider
from .dtos.common import TranscribeResult
from typing import Dict, List
from .wer import get_wer

logger: logging.Logger = logging.getLogger(__file__)


class BenchmarkABC(ABC):
    def __init__(self):
        self.__providers: Dict[str, IaProvider] = {}

    @property
    def providers(self) -> Dict[str, IaProvider]:
        return self.__providers

    @providers.setter
    def providers(self, providers: Dict[str, IaProvider]) -> None:
        if providers is None:
            raise ValueError("Providers is empty.")

        self.__providers: Dict[str, IaProvider] = providers

    @abstractmethod
    def run(self) -> None:
        raise NotImplementedError("Implement run method.")

    def add_provider(self, name: str, provider: IaProvider) -> None:
        self.providers[name] = provider

    def remove_provider(self, name: str) -> None:
        self.providers.pop(name)

    @staticmethod
    def _run_provider(
            provider: IaProvider,
            audio: str,
            reference: str,
    ) -> TranscribeResult:
        logger.debug(f"Run {provider.__class__.__name__} with audio: {audio}")
        start: float = time.time()

        hypothesis: str = provider.transcribe(audio)

        runtime: float = round((time.time() - start) * (10 ** 3), 3)

        wer: float = get_wer(reference, hypothesis)
        duration: float = utils.get_audio_duration(audio)

        return TranscribeResult(
            audio=Path(audio).name,
            ia=provider.__class__.__name__,
            params=provider.params,
            hypothesis=hypothesis,
            reference=reference,
            wer=wer,
            accuracy=round(((1 - wer) * 100), 2),
            runtime=round((runtime / 1000), 3),
            audio_duration=round((duration / 1000), 3),
            rtf=utils.get_rtf(runtime, duration)
        )

    @staticmethod
    def _get_output_filename(name: str = "benchmark") -> str:
        return f"./results/{name}_{datetime.today()}.csv"

    @staticmethod
    def _get_fieldnames() -> List[str]:
        return [
            "audio",
            "ia",
            "params",
            "reference",
            "hypothesis",
            "audio_duration",
            "runtime",
            "rtf",
            "wer",
            "accuracy"
        ]

    def _get_provider(self, name: str) -> IaProvider:
        provider: IaProvider = self.providers.get(name)
        if provider is None:
            raise KeyError(f"Provider {name} does not exists.")

        return provider
