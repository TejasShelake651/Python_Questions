import pandas as pd
from datetime import date


df = pd.read_csv("data3.csv")


df["Birth_Date"] = pd.to_datetime(df["Birth_Date"])


today = pd.Timestamp.today()

df["Age"] = today.year - df["Birth_Date"].dt.year

birthday_not_reached = (
    (today.month < df["Birth_Date"].dt.month) |
    ((today.month == df["Birth_Date"].dt.month) &
     (today.day < df["Birth_Date"].dt.day))
)

df.loc[birthday_not_reached, "Age"] -= 1

print(df)