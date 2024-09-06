# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_powerabrquery-excel-powerabrqueryabrtips-activity-7237927549903716352-fuTG/

# Read the data range
df = xl("B2:C26", headers=True)

# Perform adata munging
df = df.sort_values(by='Date') # Ensure dates are sorted
df['Cat'] = (df['Sales'] < df['Sales'].shift(1)).cumsum()

df = df.groupby('Cat').agg(
    Group=(
        'Date', lambda x: x.min().strftime('%d/%m/%Y') if x.count() == 1 
        else f'{x.min().strftime('%d/%m/%Y')}-{x.max().strftime('%d/%m/%Y')}'
    ),
    TotalSales=('Sales', 'sum')
    ).reset_index().rename(columns={'TotalSales': 'Total Sales'})

df = df[['Group', 'Total Sales']]

# Display the final results
df
