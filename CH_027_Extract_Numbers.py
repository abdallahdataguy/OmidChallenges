# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_excelchallenge-powerquerychllenge-excel-activity-7178148663230099456-UqEB/

import pandas as pd
import re

# Read the Excel file
file_path = 'CH-027 Extract Numbers.xlsx'
df = pd.read_excel(file_path, usecols='B')

# Create a function to extract numbers in parentheses from a string
def extract_numbers(col):
    return ', '.join(re.findall('\((\d+)\)', col))

# Create the results column using the above function
df['Result Tables'] = df['Question Tables'].apply(extract_numbers)
df = df['Result Tables'].str.split(', ', expand=True)
df = df.fillna('')

# Print the output
print(df)
