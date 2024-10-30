import pandas as pd
from plots.strategy import PlotStrategy
from plots.appearance import AppearanceComposite
from wavbench.utils import check_path
from typing import List, Dict, Optional


class ReportData:
    def __init__(self, input_: str) -> None:
        self.__df: pd.DataFrame = pd.read_csv(input_)

    @property
    def df(self) -> pd.DataFrame:
        return self.__df

    @df.setter
    def df(self, dataframe: pd.DataFrame) -> None:
        self.__df = dataframe

    def get_by_configs(self) -> List[pd.DataFrame]:
        """Creates a list of dataframes, each of which is a
        different configuration of a transformer"""
        return [
            self.get_by("provider_name", name)
            for name in self.get("provider_name")
        ]

    def get_by(self, column: str, value: str) -> pd.DataFrame:
        """Creates a new dataframe with the rows where the column
        has the given value."""
        return self.df[self.df[column] == value]

    def get(self, column: str) -> pd.DataFrame:
        """Creates a dataframe with the values contained
        in the column provided."""
        return self.df[column].unique()

    def group_by_mean(self, column: str) -> pd.DataFrame:
        return self.df.groupby([column]).mean(numeric_only=True)

    def rename_columns(self, columns: Dict[str, str]) -> None:
        self.df.rename(
            columns=columns,
            inplace=True,
        )

    def enumerate_index(self) -> None:
        self.df.index = [
            f"{n + 1} {name}"
            for n, name in enumerate(self.df.index.tolist())
        ]


if __name__ == "__main__":
    data: ReportData = ReportData("../../results/test.csv")
    ias = data.get_by("ia", "FasterWhisper")
    print(data.df)
    print(ias)
