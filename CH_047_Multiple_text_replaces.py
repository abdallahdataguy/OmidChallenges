# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_excelchallenge-powerquerychllenge-excel-activity-7192629058730356736-Z_TS/

import pandas as pd

# Read the Excel file
file_path = 'CH-047 Multiple text replaces.xlsx'
df = pd.read_excel(file_path, usecols='B', skiprows=1)
df1 = pd.read_excel(file_path, usecols='E:F', skiprows=1, nrows=8)

# Perform data transformation and cleansing
for i in df.index:
    for j in df1.index:
        df.iat[i, 0] = df.iat[i, 0].replace(df1.iat[j, 0], df1.iat[j, 1])

# Display the output
df
