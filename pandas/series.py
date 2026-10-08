import pandas as pd

data = pd.read_csv("data.csv")

series = pd.Series(data["Name"])

print(series)