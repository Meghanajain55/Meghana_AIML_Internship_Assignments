import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

print("Original Data:\n", df)

# 1. Handle missing values
df["Marks"].fillna(df["Marks"].mean(), inplace=True)
df["Attendance"].fillna(df["Attendance"].mean(), inplace=True)
df["Study_Hours"].fillna(df["Study_Hours"].mean(), inplace=True)

# 2. Remove duplicates
df.drop_duplicates(inplace=True)

# 3. Standardize text (Name column)
df["Name"] = df["Name"].str.strip().str.title()

# Cleaned Data
print("\nCleaned Data:\n", df)