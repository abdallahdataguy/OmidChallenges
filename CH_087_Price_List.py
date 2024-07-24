# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_excelchallenge-powerquerychallenge-excel-activity-7221620092386566144-5BYS/

# Read the data ranges
df1 = xl("B2:D9", headers=True)
df2 = xl("G2:I11", headers=True)

# Perform data munging
df3 = pd.merge(df2, df1, on='Product')
df3['Diff'] = (df3['Date'] - df3['From Date']).dt.days
df3['Diff'] = df3['Diff'].where(df3['Diff']>=0, np.nan)
df4 = df3.groupby(
    ['Date', 'Product', 'Quantity']
)['Diff'].min().reset_index()
df = pd.merge(df4, df3, on=['Product', 'Quantity', 'Diff'])

# Select the required columns
df = df.iloc[:, [0, 1, 2, 6]]
# Rename the columns
df.columns = df2.columns.tolist() + ['Price']

# Display the final results
df
