# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_powerabrquery-excel-powerabrqueryabrtips-activity-7239377104709017600-5aV-/

# Read the data range
df = xl("B2:D26", headers=True)

# Perform data manipulation
df = df.groupby('Date')['Sales'].sum().reset_index()
df = (
    df[['Date']][df['Sales'] > df['Sales'].shift(1)]
    .reset_index(drop=True)
    .rename(columns={'Date': 'Dates'})
)

# Display trhe final results
df
