# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_excelchallenge-powerquerychllenge-excel-activity-7207124582229528576-FFF1/

import pandas as pd

# Read the Excel file
file_path = 'CH-067 Index Selections.xlsx'
df = pd.read_excel(file_path, usecols='B:H', skiprows=1)

# Perform data wrangling
df = df[['Index ID']][df.apply(lambda x: sum([a < 7 for a in x[1 : ]]) > 1, axis=1)]

# Display the final output
df
