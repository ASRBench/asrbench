import sys
import time
from .dataset import Dataset
from .output import OutputABC
from .utils import get_runtime


class BenchmarkContext:
    def __init__(
            self,
            dataset: Dataset,
            output: OutputABC,
    ) -> None:
        self.__dataset: Dataset = dataset
        self.__output: OutputABC = output
        self.__total_pairs: int = len(self.__dataset.pairs)
        self._processed_pairs: int = 0
        self.__start: float = 0.0

    @property
    def output(self) -> OutputABC:
        return self.__output

    @property
    def dataset(self) -> Dataset:
        return self.__dataset

    def start_progress(self) -> None:
        self.__start = time.time()

    def reset_progress(self) -> None:
        self._processed_pairs = 0
        self.__start = time.time()

    def update_progress(self, provider_name: str) -> None:
        self._processed_pairs += 1
        self._display_message(self._get_progress_msg(provider_name))

        if self._processed_pairs == self.__total_pairs:
            self._display_message(self._get_finish_msg())

    def _get_progress_msg(self, provider: str) -> str:
        dataset: str = self.__dataset.name
        percent: float = round(
            (self._processed_pairs / self.__total_pairs) * 100,
            2
        )
        return f"\r[{percent}%] Processing pairs from {dataset} with {provider}"

    def _get_finish_msg(self) -> str:
        runtime = get_runtime(self.__start) / 60
        return f"\tFinish process in {runtime:.2f} minutes.\n"

    @staticmethod
    def _display_message(msg: str) -> None:
        sys.stdout.write(msg)
        sys.stdout.flush()
