import csv
import logging
from pprint import pprint
from .abc_benchmark import BenchmarkABC
from .dataset import Dataset
from .dtos.common import TranscribeResult
from .providers.abc_provider import IaProvider
from typing import List, Dict, Any

logger: logging.Logger = logging.getLogger(__file__)


class DatasetBenchmark(BenchmarkABC):
    def __init__(
            self,
            datasets: List[Dataset],
            name: str = "wavbench",
    ) -> None:
        super().__init__()
        self.__datasets: List[Dataset] = datasets
        self.__name: str = name

    def run(self) -> None:
        output_filename: str = self._get_output_filename(self.__name)
        fieldnames: List[str] = self._get_fieldnames()
        fieldnames.append("dataset")

        with open(output_filename, "w") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for dataset in self.__datasets:
                logger.info(f"Run wavbench with dataset: {dataset.name}")
                self._process_dataset_with_all_providers(dataset, writer)

    def run_with_provider(self, name: str) -> None:
        provider: IaProvider = self._get_provider(name)
        output_filename: str = self._get_output_filename(
            f"{self.__name}_{provider.__class__.__name__}",
        )
        fieldnames: List[str] = self._get_fieldnames()
        fieldnames.append("dataset")

        with open(output_filename, "w") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for dataset in self.__datasets:
                logger.info(
                    f"Run wavbench with provider: {name} \
                    for dataset: {dataset.name}",
                )
                for pair in dataset.pairs:
                    result: TranscribeResult = self._run_provider(
                        provider,
                        pair.audio,
                        pair.reference,
                    )

                    final_result: Dict[str, Any] = result.__dict__
                    final_result["dataset"] = dataset.name

                    pprint(final_result)
                    writer.writerow(final_result)

    def _process_dataset_with_all_providers(
            self,
            dataset: Dataset,
            writer: csv.DictWriter[str],
    ) -> None:
        for provider_name, provider in self.providers.items():
            for pair in dataset.pairs:
                result: TranscribeResult = self._run_provider(
                    provider,
                    pair.audio,
                    pair.reference
                )
                final_result: Dict[str, Any] = result.__dict__
                final_result["dataset"] = dataset.name

                pprint(final_result)
                writer.writerow(final_result)
