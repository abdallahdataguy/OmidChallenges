# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_excelchallenge-powerquerychllenge-excel-activity-7204225482182000641-Yfrm/

import pandas as pd
import re

# Read the Excel file
file_path = 'CH-063 Custom splitter.xlsx'
df = pd.read_excel(file_path, usecols='B', skiprows=1)

# Perform data wrangling
pattern = '(\d{4}/\d{1,2}/\d{1,2})([A-Z]+)(\d+)'
df[['Date', 'Product', 'Quantity']] = df['Info'].map(
    lambda x: re.findall(pattern, x)[0]).tolist()

df = df.iloc[:, 1: ]

# Display the final results
df
