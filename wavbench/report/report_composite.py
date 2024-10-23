from report_component import ReportComponent
from typing import List


class ReportComposite(ReportComponent):
    def __init__(self) -> None:
        self.__children: List[ReportComponent] = []

    def make_plots(self) -> None:
        pass

    def make_csvs(self) -> None:
        pass

    def generate_report(self) -> None:
        pass

    def add(self, component: ReportComponent) -> None:
        pass

    def remove(self, component: ReportComponent) -> None:
        pass
