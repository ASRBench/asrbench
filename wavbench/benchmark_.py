import csv
import logging
from pprint import pprint
from .abc_benchmark import BenchmarkABC
from .providers.abc_provider import IaProvider
from .transcribe import TranscribePair, TranscribeResult
from typing import Dict

logger: logging.Logger = logging.getLogger(__file__)


class Benchmark(BenchmarkABC):
    """
    """

    def __init__(self, pair: TranscribePair, providers: Dict[str, IaProvider]):
        self.__providers: Dict[str, IaProvider] = providers
        self.__audio: str = pair.audio
        self.__reference: str = pair.reference

    @property
    def providers(self) -> Dict[str, IaProvider]:
        return self.__providers

    @property
    def audio(self) -> str:
        return self.__audio

    @property
    def reference(self) -> str:
        return self.__reference

    def run(self) -> None:
        logger.info(f"Run benchmark with audio: {self.audio}")
        with open(self._get_output_filename(), "w") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self._get_fieldnames())
            writer.writeheader()

            for provider_name, provider in self.providers.items():
                result: TranscribeResult = self._run_provider(
                    provider, self.audio, self.reference,
                )

                pprint(result.to_dict())
                writer.writerow(result.to_dict())

    def run_with_provider(self, name: str) -> TranscribeResult:
        logger.info(
            f"Run benchmark with provider: {name} for audio: {self.audio}",
        )
        result = self._run_provider(
            self._get_provider(name),
            self.audio,
            self.reference,
        )

        pprint(result)

        return result
