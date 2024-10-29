import time
from .dataset import Dataset
from .observer import Observer
from typing import List


class BenchmarkContext:
    def __init__(self, datasets: List[Dataset], observer: Observer) -> None:
        self.__datasets: List[Dataset] = datasets
        self._total: int = 0
        self._current: int = 0
        self._start: float = 0.0
        self._progress: float = 0.0
        self._observer: Observer = observer
        self.__dataset = None

    @property
    def dataset(self) -> Dataset:
        if self.__dataset is None:
            raise ValueError(
                "Context dataset is none, verify benchmark run methods.",
            )

        return self.__dataset

    def set_dataset(self, idx: int) -> None:
        self.__dataset: Dataset = self.__datasets[idx]
        self._total = len(self.__dataset.pairs)

    def start_progress(self) -> None:
        self._start: float = time.time()

    def reset_progress(self) -> None:
        self._current: int = 0
        self._progress: float = 0.0

    def update_progress(self, provider_name: str) -> None:
        self._current += 1
        self._observer.update_progress(
            self._get_progress(),
            self._get_progress_msg(provider_name),
        )

        if self._current == self._total:
            self._observer.finish()

    def _get_progress(self) -> float:
        self._progress = self._current / self._total
        return self._progress

    def _get_progress_msg(self, provider: str) -> str:
        dataset: str = self.__dataset.name
        return f"Processing pairs from {dataset} with {provider}..."
