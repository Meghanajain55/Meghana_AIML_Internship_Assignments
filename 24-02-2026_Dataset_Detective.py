import pandas as pd

df = pd.read_csv("data.csv")

print("Top 5 rows:\n", df.head())

numeric_cols = df.select_dtypes(include=['number'])
max_values = numeric_cols.max()

highest_column = max_values.idxmax()
highest_value = max_values.max()

print("\nColumn with highest value:", highest_column)
print("Highest value:", highest_value)

print("\nMissing values:\n", df.isnull().sum())