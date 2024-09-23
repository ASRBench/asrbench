import csv
from .abc_benchmark import BenchmarkABC
from .dtos.common import TranscribeResult
from .providers.abc_provider import IaProvider
from typing import Dict


class Benchmark(BenchmarkABC):
    """
    """

    def __init__(self, audio, reference: str):
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

    def run(self) -> None:
        with open(self._get_output_filename(), "w") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self._get_fieldnames())
            writer.writeheader()

            for provider_name, provider in self.providers.items():
                result: TranscribeResult = self._run_provider(
                    provider, self.audio, self.reference,
                )

                # show terminal resume
                writer.writerow(result.__dict__)

    def run_with_provider(self, name: str) -> TranscribeResult:
        provider: IaProvider = self._get_provider(name)
        return self._run_provider(provider, self.audio, self.reference)
