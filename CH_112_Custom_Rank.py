# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_powerabrquery-excel-powerabrqueryabrtips-activity-7240101880893186048-WBC2/

# Read the data range
df = xl("C2:E6", headers=True)

# Perform data manipulation
df['Diff'] = df[2022] - df[2023]
df = df.sort_values(
    by='Diff', 
    ignore_index=True
)
df['Rank'] = df.index + 1
df = df[['Rank', 'Product']]

# Display the final results
df
