# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_excelchallenge-powerquerychllenge-excel-activity-7202775919751569408-nZ3l/

import pandas as pd

# Read the Excel file
file_path = 'CH-061 Sales per customer.xlsx'
df1 = pd.read_excel(file_path, usecols='B:D', skiprows=1)
df2 = pd.read_excel(file_path, usecols='F:G', skiprows=1, nrows=6)

# Perform data wrangling
for i in df1.index:
    value = df1.iat[i, 1]
    for j in df2.index:
        if df2.iat[j, 0] == value:
            value = df2.iat[j, 1]
    df1.iat[i, 1] = value

df1['Order'] = df1['Customer ID'].map(lambda x: int(x.split('-')[1]))
df = df1.groupby(['Order', 'Customer ID'])['Quantity'].sum().reset_index()
df = df.rename(columns={'Customer ID': 'Customer', 'Quantity': 'Sales'})
df = df.iloc[:, 1:]

# Display the final results
df
