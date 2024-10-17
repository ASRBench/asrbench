import csv
import logging
from pprint import pprint
from .abc_benchmark import BenchmarkABC
from .dataset import Dataset
from .transcribe import TranscribeResult
from .providers.abc_provider import IaProvider
from typing import List, Dict, Any, TextIO

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

                self._process_dataset_with_all_providers(
                    dataset,
                    writer,
                    csv_file,
                )

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
                self._process_dataset_pairs(dataset, provider, writer, csv_file)

    def _process_dataset_pairs(
            self,
            dataset: Dataset,
            provider: IaProvider,
            writer: csv.DictWriter[str],
            file: TextIO,
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
            file.flush()

    def _process_dataset_with_all_providers(
            self,
            dataset: Dataset,
            writer: csv.DictWriter[str],
            file: TextIO,
    ) -> None:
        for provider_name, provider in self.providers.items():
            provider.load()
            self._process_dataset_pairs(dataset, provider, writer, file)
            provider.unload()
