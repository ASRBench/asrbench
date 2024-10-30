from pathlib import Path
from abc import ABC, abstractmethod


class ReportTemplate(ABC):
    def generate_report(self) -> None:
        self.process_data()
        self.create_plot()
        self.apply_appearance()
        # self.save_files() ??
        self.mount_report()

    @abstractmethod
    def process_data(self) -> None:
        ...

    @abstractmethod
    def create_plot(self) -> None:
        ...

    @abstractmethod
    def apply_appearance(self) -> None:
        ...

    @abstractmethod
    def mount_report(self) -> None:
        ...


class DefaultReport(ReportTemplate):
    def __init__(self, data_file: str, output_: Path) -> None:
        self._data = data_file  # ??
        self.__output_path: Path = output_

    def process_data(self) -> None:
        ...

    def create_plot(self) -> None:
        ...

    def apply_appearance(self) -> None:
        ...

    def mount_report(self) -> None:
        ...
