# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_excelchallenge-powerquerychllenge-excel-activity-7189729963254640640-m0AH/

import pandas as pd

# Read the Excel file into multiple dataframes
file_path = 'CH-044 Combine Tables.xlsx'
df1 = pd.read_excel(file_path, usecols='C:F', skiprows=2, nrows=3)
df2 = pd.read_excel(file_path, usecols='C:G', skiprows=8, nrows=3)
df3 = pd.read_excel(file_path, usecols='C:F', skiprows=14, nrows=3)

# Perform data transformation and cleansing
df = pd.concat([df1, df2, df3]).fillna(value=0)
df[df.columns[1:]] = df[df.columns[1:]].astype(int)
df = df.groupby('Regions')[sorted(df.columns[1:])].sum()
df = df.reset_index()

# Print the output
print(df)
