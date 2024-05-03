# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_excelchallenge-powerquerychllenge-excel-activity-7191919569135890432-MEsd/

import pandas as pd

# Read the Excel file
file_path = 'CH-046 Numbers Cleaning.xlsx'
df = pd.read_excel(file_path, usecols='B', skiprows=1)
df = df.sort_values(by=df.columns[0], ignore_index=1)

# Perform data transformation and cleansing
values = []
start = df.iat[0, 0]
for i in df.index:    
    if i == 0 and df.iat[0, 0] + 1 != df.iat[1, 0]: 
        values.append(str(df.iat[0, 0]))
        start = df.iat[i + 1, 0]
    elif i == df.index[-1] and df.iat[i - 1, 0] + 1 != df.iat[i, 0]:
        values.append(str(df.iat[i, 0]))
    elif df.iat[i, 0] + 1 != df.iat[i + 1, 0] and df.iat[i, 0] == start:
        values.append(str(df.iat[i, 0]))
        start = df.iat[i + 1, 0]
    elif df.iat[i, 0] + 1 != df.iat[i + 1, 0] and df.iat[i, 0] != start:
        values.append(str(start) + '-' + str(df.iat[i, 0])[-2:])
        start = df.iat[i + 1, 0]  

# Create a dataframe of the required results
df = pd.DataFrame(values, columns=['Product ID'])

# Print the output
df
