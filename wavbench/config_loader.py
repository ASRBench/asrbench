import yaml
from .abc_benchmark import BenchmarkABC
from .providers.abc_provider import IaProvider
from .providers.factory import ProviderFactory
from .benchmark_ import Benchmark
from .dataset_benchmark import DatasetBenchmark
from .dataset import Dataset
from pathlib import Path
from typing import List, Dict, Any


class BenchmarkFactory:
    def __init__(self, config_path: str) -> None:
        self.__config_path: str = config_path
        self.__providers: Dict[str, Any]
        self.__main_cls: BenchmarkABC

    def _load_config(self) -> None:
        with open(self.__config_path, "r") as file:
            config: Dict[str, Any] = yaml.safe_load(file)

        if "datasets" in config:
            datasets: List[Dataset] = self._get_datasets(config["datasets"])
            self.__main_cls = DatasetBenchmark(datasets)

        if "audio" in config:
            audio_dict = config["audio"]
            audio: str = self._get_audio_value(audio_dict, "path")
            reference_path = Path(
                self._get_audio_value(audio_dict, "reference"),
            )
            self.__main_cls = Benchmark(audio, reference_path.open().read())

        if "providers" not in config:
            raise KeyError("Providers is missing in config file.")

        self.__main_cls.providers = self._get_providers(config["providers"])

    @staticmethod
    def _get_datasets(configs: Dict[str, Dict[str, str]]) -> List[Dataset]:
        return [
            Dataset.from_config(name, config)
            for name, config in configs.items()
        ]

    @staticmethod
    def _get_providers(
            config: Dict[str, Dict[str, Any]],
    ) -> Dict[str, IaProvider]:
        factory: ProviderFactory = ProviderFactory()
        return factory.get_providers(config)

    @staticmethod
    def _get_audio_value(audio: Dict[str, str], value: str) -> str:
        if value not in audio:
            raise KeyError(f"Audio {value} is missing in config file.")
        return audio[value]

    @classmethod
    def from_config(cls, config_path: str) -> BenchmarkABC:
        loader: BenchmarkFactory = cls(config_path)
        loader._load_config()
        return loader.__main_cls
