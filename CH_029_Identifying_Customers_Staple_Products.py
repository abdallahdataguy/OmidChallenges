# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_excelchallenge-powerquerychllenge-excel-activity-7179583105983291392-fnVE/

import pandas as pd

# Create functions to generate the required results
# Function to get the maximum values for each row given a list of columns
def maximum_value(*values):
    return max(values)

# Function to get column names where values match 'maximum value' per row
def get_products(row):
    products = [col for col in df2.columns[1:-1] if row[col] == row['maximum_value']]
    return ','.join(products)

# Read the Excel file
file_path = 'CH-029 Identifying Customers Staple Products.xlsx'
df1 = pd.read_excel(file_path, usecols='I:J', nrows=4, skiprows=1) # Original data frame
df2 = pd.read_excel(file_path, usecols='B:E', skiprows=1) # Data frame for computation
df2 = df2.pivot_table(values='Quantity', index='Customer ID', columns='Product', aggfunc='sum').fillna(0)
df2 = df2.reset_index()

# Add columns to the dataset and print the output
df2['maximum_value'] = df2.apply(lambda x: maximum_value(x['A'], x['B'], x['C'], x['D'], x['E']), axis=1)
df2['Most Purchased PRODUCT'] = df2.apply(get_products, axis=1)
df2 = df2.rename_axis(None, axis=1).rename(columns={'Customer ID': 'Customer'})

print(f'\nExpected Answer:\n{df1} \n\nMy Answer: \n{df2.iloc[:, [0, -1]]}')
