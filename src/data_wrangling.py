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

# Remove irrelevant columns
columns_to_remove = [
    'FIPS Code', 
    'Total Civilian Non-Institutional Population in State/Area', 
    'Percent (%) of State/Area’s Population'
]
df = df.drop(columns=columns_to_remove, errors='ignore')

# Convert columns from object type to int64
columns_to_convert = [
    'Total Civilian Labor Force in State/Area',
    'Total Employment in State/Area',
    'Total Unemployment in State/Area'
]

for column in columns_to_convert:
    # Remove commas and convert to int64
    df[column] = df[column].str.replace(',', '').astype(np.int64)

# Verify the conversion
print("Updated DataFrame Info:")
print(df.info())

# Save the cleaned DataFrame to a new CSV file
output_path = '../data/processed/cleaned_unemployment_in_america_per_us_state.csv'
df.to_csv(output_path, index=False)
print(f"\nCleaned data saved to {output_path}")