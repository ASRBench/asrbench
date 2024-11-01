import pandas as pd
from abc import ABC, abstractmethod
from datetime import datetime, UTC
from .input_ import Input
from jinja2 import Template
from plots.appearance import (
    AppearanceComposite,
    EnumeratePoints,
    LegendPosition,
    FacetGridAxisLabels,
)
from .plots.strategy import DispersionPlot
from .report_data import ReportData
from .template_loader import TemplateLoader
from pathlib import Path
from typing import Dict, Any
from weasyprint import HTML


class ReportTemplate(ABC):
    def generate_report(self) -> None:
        df: pd.DataFrame = self.process_data()
        self.create_plot(df)
        self.mount_report()

    @abstractmethod
    def process_data(self) -> pd.DataFrame:
        ...

    @abstractmethod
    def create_plot(self, df: pd.DataFrame) -> None:
        ...

    @abstractmethod
    def mount_report(self) -> None:
        ...


class DefaultReport(ReportTemplate):
    def __init__(self, input_: Input, output_: Path) -> None:
        self._data = ReportData(input_.read_data())
        self._output: Path = output_
        self._result: Dict[str, Any] = {"file": input_.filepath}

    def process_data(self) -> pd.DataFrame:
        mean: pd.DataFrame = self._data.group_by_mean("provider_name")

        self._result["configs"] = self._data.get_configs_dict()
        self._result["mean_stats"] = mean.to_dict(orient="index")

        return mean

    def create_plot(self, df: pd.DataFrame) -> None:
        strategy = DispersionPlot(
            x="accuracy",
            y="rft",
            hue="provider_name"
        )
        plot = strategy.plot(df)

        appearance_kit: AppearanceComposite = AppearanceComposite()
        appearance_kit.add(EnumeratePoints(df, "accuracy", "rtf"))
        appearance_kit.add(LegendPosition(plot))
        appearance_kit.add(
            FacetGridAxisLabels(
                plot=plot,
                xlabel="Accuracy (%)",
                ylabel="RTF",
                font_size=11.0,
            )
        )
        appearance_kit.customize()

        plot_output_path: str = self._output.with_suffix(".png").__str__()
        plot.savefig(plot_output_path)

        self._result["plot_title"] = "Dispersion Plot"
        self._result["plot"] = plot_output_path
        self._result["plot_description"] = """sla"""

    def mount_report(self) -> None:
        loader = TemplateLoader()
        template: Template = loader.load("default.html")

        self._result["created_at"] = datetime.now(UTC)

        HTML(
            string=template.render(**self._result),
            base_url=self._output.parent
        ).write_pdf(self._output.with_suffix(".pdf"))
