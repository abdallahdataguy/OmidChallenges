# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_excelchallenge-powerquerychllenge-excel-activity-7191179514796740608-7cqZ/

import pandas as pd
import re

# Read the Excel file
file_path = 'CH-045 Text Split.xlsx'
df = pd.read_excel(file_path, usecols='B', skiprows=1)

# Perform data transformation and cleansing
def text_split(col):
    pattern = '([A-Z]*)(\d*)([A-Z]*)(\d*)([A-Z]*)'
    return re.search(pattern, col).groups()

columns = ['Part ' + str(x) for x in range(1, 6)]
df[columns] = df['ID'].apply(text_split).tolist()
df = df.iloc[ :, 1:]

# Display the output
print(f'\nFinal Results: \n\n{df}')
