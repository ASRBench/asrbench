import pandas as pd
from pprint import pprint


# processar infos
# calcular dados
# plotar graficos
# montar pdf
# escrever e salvar arquivo

def load_csv(filepath: str) -> pd.DataFrame:
    df: pd.DataFrame = pd.read_csv(filepath)
    pprint(df)
    return df


if __name__ == "__main__":
    load_csv("./results/test.csv")
