import wavbench.utils as utils
import yaml
from .abc_benchmark import BenchmarkABC
from .benchmark import DefaultBenchmark
from .dataset import Dataset
from datetime import datetime, UTC
from .output_ctx import OutputContextABC, CsvOutputContext, JsonOutputContext
from pathlib import Path
from .providers.abc_provider import IaProvider
from .providers.abc_factory import ProviderFactoryABC
from .observer import Observer, ConsoleObserver
from typing import Dict, List, Any


class Configfile:
    def __init__(
            self,
            filepath_: str,
            factory: ProviderFactoryABC,
            observer: Observer = ConsoleObserver()
    ) -> None:
        utils.check_path(filepath_)

        self.__path: str = filepath_
        self._observer: Observer = observer
        self.__data: Dict[str, Dict[str, Any]] = self.read_data()
        self.__factory: ProviderFactoryABC = factory
        self.__output_cfg: Dict[str, str] = self.data.get("output", {})

    @property
    def data(self) -> Dict[str, Dict[str, Any]]:
        return self.__data

    def read_data(self) -> Dict[str, Any]:
        """Read config data."""
        self._observer.notify("Reading configfile...")
        with open(self.__path, "r") as file:
            config: Dict[str, Any] = yaml.safe_load(file)
        self._observer.finish()
        return config

    def set_up_benchmark(self) -> BenchmarkABC:
        self._observer.notify("Mounting Benchmark...")
        benchmark = DefaultBenchmark(
            datasets=self.get_datasets(),
            providers=self.get_providers(),
            output=self.get_output(),
            observer=self._observer,
        )
        self._observer.finish()
        return benchmark

    def get_datasets(self) -> List[Dataset]:
        if not self.has_dataset():
            raise ValueError("Configfile dont have datasets configuration.")

        return [
            Dataset.from_config(name, config)
            for name, config in self.data.get("datasets").items()
        ]

    def has_dataset(self) -> bool:
        return "datasets" in self.data

    def get_providers(self) -> Dict[str, IaProvider]:
        return self.__factory.from_config(
            self.get_config_section("providers"),
        )

    def get_output(self) -> OutputContextABC:
        type_: str = self.__output_cfg.get("type", "csv")

        match type_:
            case "csv":
                return CsvOutputContext(self.get_output_filepath())
            case "json":
                return JsonOutputContext(self.get_output_filepath())
            case _:
                raise ValueError(f"Output type {type_} not supported.")

    def set_up_output_filename(self) -> str:
        timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%S")
        return f"{self.get_output_filename()}_{timestamp}"

    def get_output_filepath(self) -> str:
        return Path(
            self.get_output_dir()
        ).joinpath(
            self.set_up_output_filename()
        ).__str__()

    def get_output_dir(self) -> str:
        return self.__output_cfg.get("dir", Path.cwd())

    def get_output_filename(self) -> str:
        return self.__output_cfg.get("filename", "asrbench")

    def get_config_section(self, section: str) -> Dict[str, Any]:
        if section not in self.data:
            raise KeyError(f"Configfile dont have {section} section.")
        return self.data[section]

    @staticmethod
    def get_config_value(section: Dict[str, Any], key: str) -> Any:
        if key not in section or section[key] is None:
            raise KeyError(f"Configfile {section} section missing {key}.")

        return section[key]
