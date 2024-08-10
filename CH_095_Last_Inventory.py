# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_powerabrquery-excel-powerabrqueryabrtips-activity-7227780686835818497-012e/

df = xl("B2:G7", headers=True)
# Perform data wrangling
df['Last Inventory'] = df.apply(
    lambda x: [v for v in x[1:] if pd.notna(v)][-1], axis=1
)
df = df[['Product', 'Last Inventory']]

# Display the final results
df
