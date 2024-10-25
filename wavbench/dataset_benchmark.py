import csv
import logging
from .abc_benchmark import BenchmarkABC
from .benchmark_context import BenchmarkContext
from .dataset import Dataset
from .transcribe import TranscribeResult
from .providers.abc_provider import IaProvider
from .output import OutputABC
from typing import List, Dict, Any

logger: logging.Logger = logging.getLogger(__file__)


class DatasetBenchmark(BenchmarkABC):
    def __init__(
            self,
            datasets: List[Dataset],
            providers: Dict[str, IaProvider],
            output: OutputABC
    ) -> None:
        self.__providers: Dict[str, IaProvider] = providers
        self.__datasets: List[Dataset] = datasets
        self.__output: OutputABC = output

    @property
    def providers(self) -> Dict[str, IaProvider]:
        return self.__providers

    def run(self) -> None:
        fieldnames: List[str] = self._get_fieldnames()
        fieldnames.append("dataset")

        for dataset in self.__datasets:
            logger.info(f"Run benchmark with dataset: {dataset.name}")
            self.__output.filepath = self._get_output_filename(dataset.name)

            with self.__output:
                self._process_dataset_with_all_providers(
                    BenchmarkContext(
                        dataset=dataset,
                        output=self.__output,
                    )
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
                self._process_dataset_pairs(
                    BenchmarkContext(
                        dataset=dataset,
                        output=self.__output,
                    ),
                    provider,
                )

    def _process_dataset_pairs(
            self,
            ctx: BenchmarkContext,
            provider: IaProvider,
    ) -> None:
        ctx.start_progress()
        for pair in ctx.dataset.pairs:
            result: TranscribeResult = self._run_provider(
                provider,
                pair.audio,
                pair.reference,
            )

            final_result: Dict[str, Any] = result.to_dict()
            final_result["dataset"] = ctx.dataset.name

            ctx.update_progress(provider.name)
            ctx.output.write_row(final_result)

    def _process_dataset_with_all_providers(
            self,
            ctx: BenchmarkContext
    ) -> None:
        for provider_name, provider in self.providers.items():
            provider.load()
            self._process_dataset_pairs(ctx, provider)
            provider.unload()
            ctx.reset_progress()
