import csv
import time
import utils
from abc import ABC, abstractmethod
from wer import get_wer
from dtos.common import TranscribeResult
from datetime import datetime
from providers.abc_provider import IaProvider
from typing import Dict, List, Any


class BenchmarkABC(ABC):

    @abstractmethod
    def run(self) -> None:
        raise NotImplementedError("Implement run method.")

    @abstractmethod
    def run_with_provider(self, name: str) -> TranscribeResult:
        raise NotImplementedError("Implement run_single_provider method.")

    @staticmethod
    def _run_provider(
            provider: IaProvider,
            audio, reference: str,
    ) -> TranscribeResult:
        start: float = time.time()

        hypothesis: str = provider.transcribe(audio)

        runtime: float = round((time.time() - start) * (10 ** 3), 3)

        wer: float = get_wer(reference, hypothesis)
        duration: float = utils.get_audio_duration(audio)

        return TranscribeResult(
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
    def _get_output_filename() -> str:
        return f"benchmark_{datetime.now()}.csv"


class DatasetBenchmark(BenchmarkABC):
    def __init__(self, dataset: str) -> None:
        self.__dataset: str = dataset

    def run(self) -> None:
        pass

    def run_with_provider(self, name: str) -> TranscribeResult:
        pass


class Benchmark(BenchmarkABC):
    """
    """

    def __init__(self, audio, reference: str):
        self.__results: List[Dict[str, Any]] = []
        self.__audio: str = audio
        self.__reference: str = reference
        self.__providers: Dict[str, IaProvider] = {}

    @property
    def audio(self) -> str:
        return self.__audio

    @property
    def reference(self) -> str:
        return self.__reference

    @property
    def providers(self) -> Dict[str, IaProvider]:
        return self.__providers

    @providers.setter
    def providers(self, providers: Dict[str, IaProvider]) -> None:
        if providers is None:
            raise ValueError("Providers is empty.")

        if providers.values() is not IaProvider:
            raise ValueError("Providers is not IaProvider.")

        self.__providers: Dict[str, IaProvider] = providers

    def add_provider(self, name: str, provider: IaProvider) -> None:
        self.providers[name] = provider

    def remove_provider(self, name: str) -> None:
        self.providers.pop(name)

    def run(self) -> None:
        with open(self._get_output_filename(), "w") as csv_file:
            fieldnames: List[str] = [
                'ia',
                'params',
                'reference',
                'hypothesis',
                'audio_duration',
                'runtime',
                'rtf',
                'wer',
                'accuracy'
            ]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for provider_name, provider in self.providers.items():
                result: TranscribeResult = self._run_provider(
                    provider, self.audio, self.reference,
                )

                # show terminal resume
                writer.writerow(result.__dict__)

    def run_with_provider(self, name: str) -> TranscribeResult:
        provider: IaProvider = self.providers.get(name)
        if provider is None:
            raise KeyError(f"Provider {name} does not exists.")

        return self._run_provider(provider, self.audio, self.reference)
