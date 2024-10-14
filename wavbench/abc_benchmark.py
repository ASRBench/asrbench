import logging
import time
import wavbench.utils as utils
from abc import ABC, abstractmethod
from datetime import datetime, UTC
from pathlib import Path
from .providers.abc_provider import IaProvider
from .dtos.common import TranscribeResult, Measures
from typing import Dict, List
from .measures import get_measures, normalize_txt

logger: logging.Logger = logging.getLogger(__file__)


class BenchmarkABC(ABC):
    def __init__(self) -> None:
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

    # @abstractmethod
    # def run_with_gen_progress(self) -> Generator[Dict[str, Any], None, None]:
    # raise NotImplementedError("Implement run with progress method.")

    def add_provider(self, name: str, provider: IaProvider) -> None:
        if not isinstance(provider, IaProvider):
            raise ValueError(f"Provider {name} is not instance of IaProvider")

        self.providers[name] = provider

    def remove_provider(self, name: str) -> None:
        if name not in self.providers:
            raise KeyError(f"Provider {name} does not exists.")

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
        duration: float = utils.get_audio_duration(audio)

        measures: Measures = get_measures(reference, hypothesis)

        return TranscribeResult(
            audio=Path(audio).name,
            provider_name=provider.name,
            ia=provider.__class__.__name__,
            params=provider.params,
            hypothesis=normalize_txt(hypothesis),
            reference=normalize_txt(reference),
            measures=measures,
            accuracy=round(((1 - measures.wer) * 100), 2),
            runtime=round((runtime / 1000), 3),
            audio_duration=round((duration / 1000), 3),
            rtf=utils.get_rtf(runtime, duration)
        )

    @staticmethod
    def _get_output_filename(name: str = "wavbench") -> str:
        timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%S")
        return f"./results/{name}_{timestamp}.csv"

    @staticmethod
    def _get_fieldnames() -> List[str]:
        return [
            "audio",
            "ia",
            "provider_name",
            "params",
            "reference",
            "hypothesis",
            "audio_duration",
            "runtime",
            "rtf",
            "wer",
            "wil",
            "wip",
            "cer",
            "mer",
            "accuracy"
        ]

    def _get_provider(self, name: str) -> IaProvider:
        provider: IaProvider = self.providers.get(name)
        if provider is None:
            raise KeyError(f"Provider {name} does not exists.")

        return provider
