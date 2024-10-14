import csv
import logging
from pprint import pprint
from .abc_benchmark import BenchmarkABC
from .dataset import Dataset
from .transcribe import TranscribeResult, TranscribePair
from .providers.abc_provider import IaProvider
from typing import List, Dict, Any

logger: logging.Logger = logging.getLogger(__file__)


class DatasetBenchmark(BenchmarkABC):
    def __init__(
            self,
            datasets: List[Dataset],
            providers: Dict[str, IaProvider],
    ) -> None:
        self.__providers: Dict[str, IaProvider] = providers
        self.__datasets: List[Dataset] = datasets

    @property
    def providers(self) -> Dict[str, IaProvider]:
        return self.__providers

    def run(self) -> None:
        fieldnames: List[str] = self._get_fieldnames()
        fieldnames.append("dataset")

        for dataset in self.__datasets:
            logger.info(f"Run benchmark with dataset: {dataset.name}")
            output_filename: str = self._get_output_filename(dataset.name)

            with open(output_filename, "w") as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()

                self._process_dataset_with_all_providers(dataset, writer)

    def run_with_provider(self, name: str) -> None:
        provider: IaProvider = self._get_provider(name)
        fieldnames: List[str] = self._get_fieldnames()
        fieldnames.append("dataset")

        for dataset in self.__datasets:
            logger.info(
                f"Run wavbench with provider: {name} \
                    for dataset: {dataset.name}",
            )
            output_filename: str = self._get_output_filename(
                f"{dataset.name}_{provider.name}"
            )

            with open(output_filename, "w") as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                self._process_dataset_pairs(dataset, provider, writer)

    def _process_dataset_pairs(
            self,
            dataset: Dataset,
            provider: IaProvider,
            writer: csv.DictWriter[str],
    ) -> None:
        for pair in dataset.pairs:
            result: TranscribeResult = self._run_provider(
                provider,
                pair.audio,
                pair.reference,
            )

            final_result: Dict[str, Any] = result.to_dict()
            final_result["dataset"] = dataset.name

            pprint(final_result)
            writer.writerow(final_result)

    def _process_dataset_with_all_providers(
            self,
            dataset: Dataset,
            writer: csv.DictWriter[str],
    ) -> None:
        for provider_name, provider in self.providers.items():
            self._process_dataset_pairs(dataset, provider, writer)
