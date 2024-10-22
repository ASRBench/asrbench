import pandas as pd
from plot_strategy import PlotStrategy
from typing import List


class ReportData:
    def __init__(self, filepath_: str) -> None:
        self.__df: pd.DataFrame = pd.read_csv(filepath_)

    @property
    def df(self) -> pd.DataFrame:
        return self.__df

    @df.setter
    def df(self, dataframe: pd.DataFrame) -> None:
        self.df = dataframe

    def get_by_config(self) -> List[pd.DataFrame]:
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

    def plot(self, strategy: PlotStrategy) -> None:
        """HERE?????"""
        strategy.plot(self.df)


if __name__ == "__main__":
    data: ReportData = ReportData("../../results/test.csv")
    ias = data.get_by("ia", "FasterWhisper")
    print(data.df)
    print(ias)
