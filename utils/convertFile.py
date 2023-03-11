import pandas as pd

read_file = pd.read_excel ("GAP Analysis.xlsx")

read_file.to_csv ("GAP Analysis.csv", index = None, header=True)