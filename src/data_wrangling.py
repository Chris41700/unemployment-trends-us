import numpy as np
import pandas as pd

# Load the dataset
try:
    df = pd.read_csv('../data/raw/Unemployment in America Per US State.csv')
    print("File loaded successfully.")
except FileNotFoundError:
    print("File not found. Please check the file path.")
    exit()

if df.empty:
    print("The DataFrame is empty. Please check the dataset.")
else:
    print("The DataFrame is not empty. Here are the first few rows:")
    print(df.head()) # Load the DataFrame

# Display basic info and statistics about the DataFrame
print(df.info())
print(df.describe())

# Check for null values in the DataFrame
null_values = df.isnull().sum()

# Print the number of null values in each column
print("\nNull values in each column:")
print(null_values)

# Check for duplicate rows
duplicates = df.duplicated()
print("Number of duplicate rows:", duplicates.sum())

 