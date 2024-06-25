# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_excelchallenge-powerquerychllenge-excel-activity-7211473239376637954-5PJK/

import pandas as pd
import re

# Read the Excel file
file_path = 'CH-073 Custom splitter 2.xlsx'
df = pd.read_excel(file_path, skiprows=1, usecols='B', nrows=13)

# Perform data wrangling
df['Date'] = df['Info'].map(lambda x: re.findall(r'\d+/\d+/\d+', x)[0])
df['Other'] = df['Info'].map(
    lambda x: [', '.join(y) for y in re.findall(r'([A-Z]+)(\d+)', x)])
df = df.explode(column='Other', ignore_index=True)
df = pd.concat([df, df['Other'].str.split(', ', expand=True)], axis=1)
df = df.iloc[:, [1, 3, 4]]
df.columns = ['Date', 'Product', 'Quantity']

# Display the final dataset
df
