# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_excelchallenge-powerquerychllenge-excel-activity-7204950257233764352-a8WD/

import pandas as pd

# Read the Excel file
file_path = 'CH-064 Text Cleaning.xlsx'
df = pd.read_excel(file_path, usecols='B', skiprows=1, nrows=7)

# Perform data wrangling
df = pd.concat([df, df.Description.str.split(', ', expand=True)], axis=1)
df['Order'] = df.index
df = pd.melt(df, id_vars=['Order', 0], value_vars=df.columns[1:])
df = df.dropna()
df = pd.concat([df, df.value.str.split(' ', expand=True)], axis=1)
df = df.fillna(1).sort_values(by='Order', ignore_index=True)
df = df.iloc[:, [1, 4, 5]]
df.columns = ['Date', 'Product', 'Quantity']
df['Date'] = df['Date'].astype('datetime64[ns]')
df['Date'] = df['Date'].dt.strftime('%d/%m/%Y')

# Display the final dataset
df
