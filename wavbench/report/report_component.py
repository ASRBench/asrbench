from abc import ABC, abstractmethod


class ReportComponent(ABC):
    @abstractmethod
    def make_plots(self) -> None:
        raise NotImplementedError("Implement make_plots method.")

    @abstractmethod
    def make_csvs(self) -> None:
        raise NotImplementedError("Implement make_csvs method.")

    @abstractmethod
    def generate_report(self) -> None:
        raise NotImplementedError("Implement generate_report.")
