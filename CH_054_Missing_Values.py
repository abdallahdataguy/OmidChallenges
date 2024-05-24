# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_excelchallenge-powerquerychllenge-excel-activity-7197702500592832512-2OK8/

import pandas as pd
from datetime import datetime
from calendar import monthrange

# Read the Excel file
file_path = 'CH-054 Missing Values.xlsx'
df1 = pd.read_excel(file_path, usecols='B:D', skiprows=1, nrows=19)

# Perform data wrangling
end_dates = [(j, i) for i in list('ABC') for j in 
          [datetime(2023, x, monthrange(2023, x)[1]) for x in range(1, 13)]]
df2 = pd.DataFrame(end_dates, columns=['Date', 'Project'])
df = pd.merge(df2, df1, how='left', on=['Date', 'Project']).ffill()
df['Actual Progress'] = df['Actual Progress'].map(lambda x: f'{x:.0%}')

# Display sample output
df.head(18)
