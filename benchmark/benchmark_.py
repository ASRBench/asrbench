import csv
from .abc_benchmark import BenchmarkABC
from .dtos.common import TranscribeResult
from .providers.abc_provider import IaProvider


class Benchmark(BenchmarkABC):
    """
    """

    def __init__(self, audio, reference: str):
        super().__init__()
        self.__audio: str = audio
        self.__reference: str = reference

    @property
    def audio(self) -> str:
        return self.__audio

    @property
    def reference(self) -> str:
        return self.__reference

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
