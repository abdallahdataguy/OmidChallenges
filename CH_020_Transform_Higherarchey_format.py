# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_excelchallenge-powerquerychllenge-excel-activity-7173075223699812352-N8wT/

import pandas as pd

# Read the Excel file
file_path = 'CH-020 Transform Higherarchey format.xlsx'
df = pd.read_excel(file_path, usecols='B:C', skiprows=1)

# Data transformation and cleansing
df1 = df[df['Code'] > 99]
df1 = df1[['Code']].astype(str)
for i in range(1, 4):
    df1[i] = df1['Code'].str[: i]  
df['Code'] = df['Code'].astype(str)
df1 = df1.drop(columns='Code')
for i in [x for x in df1.columns if x < 5]:
    df1 = pd.merge(df1, df, left_on=i, right_on='Code', how='inner') 
df = df1[['Code', 'Description_x', 'Description_y', 'Description']]
df = df.rename(columns={'Description_x': 'Level 1', 'Description_y': 'Level 2', 'Description': 'Level 3'})

# Print the required output
print(f'\n{df}')
