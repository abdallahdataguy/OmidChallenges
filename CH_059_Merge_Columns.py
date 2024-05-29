# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_excelchallenge-powerquerychllenge-excel-activity-7201326372399554560-pza3/

import pandas as pd

# Read the Excel file
file_path = 'CH-059 Merge Columns.xlsx'
df = pd.read_excel(file_path, usecols='B:J', skiprows=1)

# Perform data wrangling
cols = range(1, len(df.columns), 2)
items = [[df.iat[i, 0]] 
         + [sum(df.iloc[i, j : j + 2]) for j in cols] for i in df.index]
df = pd.DataFrame(items, columns=[df.columns[[0, 1, 3, 5, 7]]])

# Display the final results
df
