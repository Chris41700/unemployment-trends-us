import numpy as np
import pandas as pd

# Load the dataset
try:
    df = pd.read_csv('../data/raw/Unemployment in America Per US State.csv')
    print("File loaded successfully.")
except FileNotFoundError:
    print("File not found. Please check the file path.")
    exit()

# Load the DataFrame
print(df.head())

# Check for null values in the DataFrame
null_values = df.isnull().sum()

# Print the number of null values in each column
print("\nNull values in each column:")
print(null_values)

