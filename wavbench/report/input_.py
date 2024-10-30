import pandas as pd
from abc import ABC, abstractmethod
from wavbench.utils import check_path


class Input(ABC):
    @abstractmethod
    def read_data(self) -> pd.DataFrame:
        raise NotImplementedError("Implement read_data method.")


class JsonInput(Input):
    def __init__(self, filepath_: str) -> None:
        check_path(filepath_)
        self._filepath: str = filepath_

    def read_data(self) -> pd.DataFrame:
        return pd.read_json(self._filepath)


class CsvInput(Input):
    def __init__(self, filepath_: str) -> None:
        check_path(filepath_)
        self._filepath: str = filepath_

    def read_data(self) -> pd.DataFrame:
        return pd.read_csv(self._filepath)
