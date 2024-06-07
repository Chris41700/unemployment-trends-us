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

annual_data = df.groupby(['Year'])[numerical_columns].mean().reset_index()
