import csv
from pprint import pprint
from .abc_benchmark import BenchmarkABC
from .dataset import Dataset
from .dtos.common import TranscribeResult
from .providers.abc_provider import IaProvider


class DatasetBenchmark(BenchmarkABC):
    def __init__(self, dataset: Dataset) -> None:
        super().__init__()
        self.__dataset: Dataset = dataset

    def run(self) -> None:
        with open(
                self._get_output_filename(self.__dataset.name),
                "w",
        ) as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self._get_fieldnames())
            writer.writeheader()

            for provider_name, provider in self.providers.items():
                for pair in self.__dataset.pairs:
                    result: TranscribeResult = self._run_provider(
                        provider,
                        pair.audio,
                        pair.reference
                    )

                    pprint(result.__dict__)
                    writer.writerow(result.__dict__)

    def run_with_provider(self, name: str) -> None:
        provider: IaProvider = self._get_provider(name)

        with open(
                self._get_output_filename(f"{self.__dataset.name}_{name}"),
                "w",
        ) as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self._get_fieldnames())
            writer.writeheader()

            for pair in self.__dataset.pairs:
                result: TranscribeResult = self._run_provider(
                    provider,
                    pair.audio,
                    pair.reference,
                )

                pprint(result.__dict__)
                writer.writerow(result.__dict__)
