# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_excelchallenge-powerquerychllenge-excel-activity-7212198020140998658-iC5E/

import pandas as pd

# Read the Excel file
file_path = 'CH-074 Determining missing fields.xlsx'
df = pd.read_excel(file_path, skiprows=1, usecols='B:C')

# Perform data wrangling
df['Order'] = df['Info'].eq('Name').cumsum()
dets = df['Info'].unique()
o, i = df['Order'], df['Info']

values = []
for n in df['Order'].unique():
    missing = ', '.join([x for x in dets if len(df[(o == n) & (i == x)]) == 0])
    duplicate = ', '.join([x for x in dets if len(df[(0 == n) & (i == x)]) > 1])
    values.append([n, missing, duplicate])

df = pd.DataFrame(values, columns=['Record No', 'Missing Fields', 'Duplicate fields'])
df = df.replace('', '-')

# Display the final dataset
df
