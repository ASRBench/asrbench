import wavbench.utils as utils
import yaml
from .abc_benchmark import BenchmarkABC
from .benchmark_ import Benchmark
from .dataset_benchmark import DatasetBenchmark
from .dataset import Dataset
from pathlib import Path
from .providers.abc_provider import IaProvider
from .providers.factory import ProviderFactory
from .transcribe import TranscribePair
from typing import Dict, List, Any


class Configfile:
    def __init__(self, filepath_: str) -> None:
        utils.check_path(filepath_)

        self.__path: str = filepath_
        self.__data: Dict[str, Dict[str, Any]] = self._read_data()

    @property
    def data(self) -> Dict[str, Dict[str, Any]]:
        return self.__data

    @property
    def filepath(self) -> str:
        return self.__path

    @filepath.setter
    def filepath(self, filepath_: str) -> None:
        utils.check_path(filepath_)
        self.__path = filepath_

    def set_up_benchmark(self) -> BenchmarkABC:
        if self.has_dataset():
            return DatasetBenchmark(
                self.get_datasets(),
                self.get_providers(),
            )

        if self.has_audio():
            return Benchmark(
                self.get_audio_config(),
                self.get_providers()
            )

        raise SyntaxError("Invalid configfile syntax.")

    def has_audio(self) -> bool:
        return "audio" in self.data

    def has_dataset(self) -> bool:
        return "datasets" in self.data

    def get_datasets(self) -> List[Dataset]:
        if not self.has_dataset():
            raise ValueError("Configfile dont have datasets configuration.")

        return [
            Dataset.from_config(name, config)
            for name, config in self.data.get("datasets").items()
        ]

    def get_audio_config(self) -> TranscribePair:
        audio_section: Dict[str, Any] = self._get_config_section("audio")

        return TranscribePair(
            audio_path=self._get_config_value(audio_section, "path"),
            reference=Path(
                self._get_config_value(audio_section, "reference"),
            ).open().read()
        )

    def get_providers(self) -> Dict[str, IaProvider]:
        provider_factory = ProviderFactory()
        return provider_factory.get_providers(
            self._get_config_section("providers"),
        )

    def _read_data(self) -> Dict[str, Any]:
        """Read config data."""
        with open(self.__path, "r") as file:
            config: Dict[str, Any] = yaml.safe_load(file)

        return config

    def _get_config_section(self, section: str) -> Dict[str, Any]:
        if section not in self.data:
            raise KeyError(f"Configfile dont have {section} section.")
        return self.data[section]

    @staticmethod
    def _get_config_value(section: Dict[str, Any], name: str) -> Any:
        if name not in section or section[name] is None:
            raise KeyError(f"Configfile {section} section missing {name}.")

        return section[name]
