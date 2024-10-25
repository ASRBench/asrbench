from __future__ import annotations

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from abc import ABC, abstractmethod
from .axis_labels import AxisLabelsStrategy
from .colors_ import generate_palette
from typing import List, Any, Tuple, Dict, Hashable


class AppearanceComponent(ABC):
    @abstractmethod
    def customize(self) -> None:
        raise NotImplementedError("Implement customize method.")

    @property
    def class_name(self) -> str:
        return self.__class__.__name__

    def add(self, child: AppearanceComponent) -> None:
        pass

    def remove(self, child: AppearanceComponent) -> None:
        pass


class AppearanceComposite(AppearanceComponent):
    def __init__(self) -> None:
        self.__children: List[AppearanceComponent] = []

    def customize(self) -> None:
        for child in self.__children:
            child.customize()

    def add(self, child: AppearanceComponent) -> None:
        self.__children.append(child)

    def remove(self, child: AppearanceComponent) -> None:
        if child not in self.__children:
            raise ValueError(f"Component {child.class_name} not in children")


class LegendPosition(AppearanceComponent):
    def __init__(
            self,
            ax: Any,
            loc: str = "upper left",
            anchor: Tuple[float] = (0.75, 1.0),
            frame_on: bool = True,
    ) -> None:
        self._ax: Any = ax
        self._loc: str = loc
        self._anchor: Tuple[float] = anchor
        self._frame_on: bool = frame_on

    def customize(self) -> None:
        sns.move_legend(
            obj=self._ax,
            loc=self._loc,
            bbox_to_anchor=self._anchor,
            frameon=self._frame_on,
        )


class RandomPalette(AppearanceComponent):
    def __init__(self, length: int) -> None:
        self.__length: int = length

    def customize(self) -> None:
        palette: List[Tuple[float, ...]] = generate_palette(self.__length)
        sns.set_palette(palette)


class FacetGridAxisLabels(AppearanceComponent):
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

    def customize(self) -> None:
        self.__plot.set_axis_labels(
            x_var=self.__xlabel,
            y_var=self.__ylabel,
            fontsize=self.__font_size,
        )


class JointGridAxisLabels(AppearanceComponent):
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

    def customize(self) -> None:
        self.__plot.set_axis_labels(
            xlabel=self.__xlabel,
            ylabel=self.__ylabel,
            fontsize=self.__font_size,
        )


class NamedPoints(AppearanceComponent):

    def __init__(self, df: pd.DataFrame, x_axis: str, y_axis: str) -> None:
        self.__df: pd.DataFrame = df
        self._x: str = x_axis
        self._y: str = y_axis

    def customize(self) -> None:
        palette: Dict[Hashable, Any] = _get_plot_palette(self.__df)

        for _, point in self.__df.iterrows():
            plt.text(
                point[self._x] + 0.005,
                point[self._y] + 0.005,
                str(point.name),
                ha="left",
                va="bottom",
                fontsize=8,
                color=palette[point.name]
            )


class EnumeratePoints(AppearanceComponent):
    def __init__(self, df: pd.DataFrame, x_axis: str, y_axis: str) -> None:
        self.__df: pd.DataFrame = df
        self._x: str = x_axis
        self._y: str = y_axis

    def customize(self) -> None:
        palette: Dict[Hashable, Any] = _get_plot_palette(self.__df)
        numbers = list(range(1, len(self.__df.index.tolist()) + 1))

        for i, point in self.__df.iterrows():
            plt.text(
                point[self._x] + 0.005,
                point[self._y] + 0.005,
                str(numbers.pop(0)),
                ha="left",
                va="bottom",
                fontsize=8,
                color=palette[point.name]
            )


def _get_plot_palette(df: pd.DataFrame) -> Dict[Hashable, Any]:
    hue_values = df.index.tolist()
    return dict(
        zip(
            hue_values,
            sns.color_palette(
                n_colors=len(hue_values),
            ),
        )
    )
