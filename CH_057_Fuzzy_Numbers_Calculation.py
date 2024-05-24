# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_excelchallenge-powerquerychllenge-excel-activity-7199876815606210560-F1-7/

import pandas as pd
import numpy as np

# Read the Excel file
file_path = 'CH-57 Fuzzy Numbers Calculation.xlsx'
df = pd.read_excel(file_path, usecols='B:C', skiprows=1)

# Perform data wrangling
def fuzzy_calc(col1, col2):
    a, b = np.array(col1.split(','), int), np.array(col2.split(','), int)
    result = ','.join(map(str, a + b)), ','.join(map(str, a - b[::-1]))
    return result
    
df[['A+B', 'A-B']] = df.apply(lambda x: fuzzy_calc(x[0], x[1]), axis=1).tolist()

# Display the final results
df.iloc[:, -2:]
