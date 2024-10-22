import pandas as pd
from abc import ABC, abstractmethod


class PlotStrategy(ABC):

    @abstractmethod
    def plot(self, df: pd.DataFrame) -> None:
        raise NotImplementedError("Implement plot method.")


class DispersionPlot(PlotStrategy):

    def plot(self, df: pd.DataFrame) -> None:
        ...


class BarPlot(PlotStrategy):

    def plot(self, df: pd.DataFrame) -> None:
        ...
