import seaborn as sns
from abc import ABC, abstractmethod


class AxisLabelsStrategy(ABC):
    @abstractmethod
    def set(self) -> None:
        raise NotImplementedError("Implement set method.")


class FacetGridAxisLabels(AxisLabelsStrategy):
    def __init__(
            self,
            plot: sns.FacetGrid,
            xlabel: str,
            ylabel: str,
            font_size: float = 10.0,
    ) -> None:
        self.__plot: sns.FacetGrid = plot
        self.__xlabel: str = xlabel
        self.__ylabel: str = ylabel
        self.__font_size: float = font_size

    def set(self) -> None:
        self.__plot.set_axis_labels(
            x_var=self.__xlabel,
            y_var=self.__ylabel,
            fontsize=self.__font_size,
        )


class JointGridAxisLabels(AxisLabelsStrategy):
    def __init__(
            self,
            plot: sns.JointGrid,
            xlabel: str,
            ylabel: str,
            font_size: float = 10.0,
    ) -> None:
        self.__plot: sns.JointGrid = plot
        self.__xlabel: str = xlabel
        self.__ylabel: str = ylabel
        self.__font_size: float = font_size

    def set(self) -> None:
        self.__plot.set_axis_labels(
            xlabel=self.__xlabel,
            ylabel=self.__ylabel,
            fontsize=self.__font_size,
        )
