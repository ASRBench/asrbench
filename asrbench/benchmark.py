import time
import logging
from . import jiwer_
from . import utils
from .abc_benchmark import BenchmarkABC
from .benchmark_context import BenchmarkContext
from .dataset import Dataset
from .transcribe import TranscribeResult, TranscribePair, Measures
from .transcribers.abc_transcriber import Transcriber
from .observer import Observer
from .output_ctx import OutputContextABC
from typing import List, Dict, Any

logger: logging.Logger = logging.getLogger(__file__)


class DefaultBenchmark(BenchmarkABC):
    def __init__(
            self,
            datasets: List[Dataset],
            transcribers: Dict[str, Transcriber],
            output: OutputContextABC,
            observer: Observer,
    ) -> None:
        self.__providers: Dict[str, Transcriber] = transcribers
        self.__datasets: List[Dataset] = datasets
        self.__output: OutputContextABC = output
        self._observer: Observer = observer
        self._context: BenchmarkContext = BenchmarkContext(datasets, observer)

    @property
    def transcribers(self) -> Dict[str, Transcriber]:
        return self.__providers

    def run(self) -> str:
        with self.__output:
            for idx, dataset in enumerate(self.__datasets):
                logger.info(f"Run benchmark for dataset: {dataset.name}")
                self._context.set_dataset(idx)
                self._process_dataset_with_providers()
        return self.__output.filepath

    def run_with_transcriber(self, name: str) -> str:
        with self.__output:
            for idx, dataset in enumerate(self.__datasets):
                logger.info(
                    f"Run benchmark with provider: {name}"
                    f"for dataset: {dataset.name}",
                )

                self._context.set_dataset(idx)
                self._process_dataset_pairs(self._get_provider(name))
        return self.__output.filepath

    def _process_dataset_pairs(self, provider: Transcriber) -> None:
        self._context.start_progress()
        for pair in self._context.dataset.pairs:
            result: TranscribeResult = self._run_transcribe(
                provider,
                pair,
            )

            final_result: Dict[str, Any] = result.to_dict()

            self._context.update_progress(provider.name)
            self.__output.write_row(final_result)

    def _process_dataset_with_providers(self) -> None:
        for provider_name, provider in self.transcribers.items():
            provider.load()
            self._process_dataset_pairs(provider)
            provider.unload()
            self._context.reset_progress()

    def _get_provider(self, name: str) -> Transcriber:
        if name not in self.__providers:
            raise KeyError(f"Provider {name} not in benchmark providers.")

        return self.__providers[name]

    def _run_transcribe(
            self,
            provider: Transcriber,
            pair: TranscribePair,
    ) -> TranscribeResult:
        audio_path: str = pair.audio
        reference: str = pair.reference

        logger.debug(
            f"Run {provider.__class__.__name__} with audio: {audio_path}",
        )

        start: float = time.time()
        hypothesis: str = provider.transcribe(audio_path)
        runtime: float = utils.get_runtime(start)
        duration: float = utils.get_audio_duration(audio_path)

        measures: Measures = jiwer_.get_measures(reference, hypothesis)

        return TranscribeResult(
            audio=utils.get_filename(audio_path),
            transcriber_name=provider.name,
            asr=provider.__class__.__name__,
            params=provider.params,
            hypothesis=jiwer_.normalize_txt(hypothesis),
            reference=jiwer_.normalize_txt(reference),
            measures=measures,
            accuracy=round(((1 - measures.wer) * 100), 2),
            runtime=runtime,
            audio_duration=duration,
            rtf=utils.get_rtf(runtime, duration),
            dataset=self._context.dataset.name,
        )