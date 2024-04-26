# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_excelchallenge-powerquerychllenge-excel-activity-7189729963254640640-m0AH/

import pandas as pd

# Read the Excel file
file_path = 'CH-043 Sort Table columns .xlsx'
df = pd.read_excel(file_path, usecols='B:G', nrows=8, skiprows=1)

# Perform data transformation and cleansing
totals = df.iloc[:, 1:].sum()
df1 = df[totals.sort_values(ascending=False).index] # sorted df
df = pd.concat([df.iloc[:, 0], df1], axis=1)

# Print the output
df
