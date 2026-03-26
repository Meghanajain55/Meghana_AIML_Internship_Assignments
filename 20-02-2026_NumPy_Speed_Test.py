import pandas as pd

df = pd.read_csv("data.csv")

print("Top 5 rows:\n", df.head())

numeric_cols = df.select_dtypes(include='number')
max_values = numeric_cols.max()

print("\nColumn with highest value:", max_values.idxmax())
print("Highest value:", max_values.max())

print("\nMissing values:\n", df.isnull().sum())