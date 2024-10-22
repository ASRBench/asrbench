import pandas as pd
from report_data import ReportData

"""
para cada benchmark separar cada IA para cada configuracao e fazer a 
media dos measures.
talvez juntar cada series de media e plotar um grafico de dispercao.
fazer esse processo para cada dataset.
"""

if __name__ == "__main__":
    data: ReportData = ReportData("../../results/test.csv")

    for df in data.get_by_config():
        print(df.describe().T['mean'])
