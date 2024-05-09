# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_excelchallenge-powerquerychllenge-excel-activity-7194078630744842240-MlNb/

import pandas as pd

# Read the Excel file
file_path = 'CH-049 Assignment Problem Part 1.xlsx'
df = pd.read_excel(file_path, usecols='B:F', skiprows=1, index_col=0)

# Perform data transformation and cleansing
df = df.apply(lambda x: x - min(x), axis=1).apply(lambda x: x - min(x))

# Display the results
df
