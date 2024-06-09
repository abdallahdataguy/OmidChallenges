# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_excelchallenge-powerquerychllenge-excel-activity-7205675021820657666-Jh6z/

import pandas as pd

# Read the Excel file
file_path = 'CH-065 Transformation.xlsx'
df = pd.read_excel(file_path, usecols='B:D', skiprows=1, nrows=4)

# Perform data wrangling
df['Date'] = df.apply(lambda x: pd.date_range(start=x[0], end=x[1]), axis=1)
df['Interval'] = df['Date'].map(len)
df['AVG Cost'] = (df['Cost'] / df['Interval']).astype(int)
df = df[['Date', 'AVG Cost']]
df = df.explode(column='Date', ignore_index=True)

# Display the final datset
df
