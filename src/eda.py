import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv('../data/processed/cleaned_unemployment_in_america_per_us_state.csv')

# Plotting distributions of numeric columns
numerical_columns = [
    'Total Civilian Labor Force in State/Area',
    'Total Employment in State/Area',
    'Total Unemployment in State/Area',
    'Percent (%) of State/Area\'s Population',
    'Percent (%) of Labor Force Employed in State/Area',
    'Percent (%) of Labor Force Unemployed in State/Area'
]

# Aggregate the data by year (mean)
annual_data = df.groupby(['Year'])[numerical_columns].mean().reset_index()

# Plot histograms for each numerical column (aggregated by year)
# for column in numerical_columns:
#     plt.figure(figsize=(10, 6))
#     plt.hist(annual_data[column], bins=30, edgecolor='k', alpha=0.7)
#     plt.title(f'Histogram of {column} (Aggregated by Year)')
#     plt.xlabel(column)
#     plt.ylabel('Frequency')
#     plt.grid(True)
#     plt.show()

# Create a dictionary to store the statistics
stats = {}

# Calculate the statistics for each column
for column in numerical_columns:
    stats[column] = {
        'Sum': df[column].sum(),
        'Mean': df[column].mean(),
        'Median': df[column].median(),
        'Standard Deviation': df[column].std(),
        'Minimum': df[column].min(),
        'Maximum': df[column].max()
    }

# Convert the dictionary to a DataFrame for better visualization
stats_df = pd.DataFrame(stats)
print(stats_df)

# Subgroup size by State/Area
state_pivot = df.pivot_table(index='State/Area', aggfunc='size').reset_index(name='Record Count')
print(state_pivot)

# Subgroup size by Year
year_pivot = df.pivot_table(index='Year', aggfunc='size').reset_index(name='Record Count')
print(year_pivot)

# Subgroup size by Month
month_pivot = df.pivot_table(index='Month', aggfunc='size').reset_index(name='Record Count')
print(month_pivot)

# Aggregate the data by month to see seasonality trends
monthly_data = df.groupby(['Year', 'Month']).mean().reset_index()

# Create a column for date to facilitate plotting
monthly_data['Date'] = pd.to_datetime(monthly_data[['Year', 'Month']].assign(DAY=1))

# Plot Total Employment by month
plt.figure(figsize=(14, 7))
sns.lineplot(data=monthly_data, x='Date', y='Total Employment in State/Area')
plt.title('Monthly Total Employment in the United States (1976-2022)')
plt.xlabel('Date')
plt.ylabel('Total Employment')
plt.grid(True)
plt.show()

# Plot Total Unemployment by month
plt.figure(figsize=(14, 7))
sns.lineplot(data=monthly_data, x='Date', y='Total Unemployment in State/Area')
plt.title('Monthly Total Unemployment in the United States (1976-2022)')
plt.xlabel('Date')
plt.ylabel('Total Unemployment')
plt.grid(True)
plt.show()
