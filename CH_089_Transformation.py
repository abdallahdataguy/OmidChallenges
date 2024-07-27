# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_excelchallenge-powerquerychallenge-excel-activity-7223069649310040064-7sTA/

# Read the data range
df = xl("B2:G10", headers=True)

# Perform data munging
cols = df.columns
cols = [col if col else cols[key - 1] for key, col in enumerate(cols)]
cols = ['_'.join(x) for x in zip(df.iloc[0], cols)]
df.columns = cols
df = df.drop(0).reset_index()
df = df.melt(id_vars='index', value_vars=df.columns[1:]).dropna()
df[['Category', 'Product']] = df['variable'].str.split('_').tolist()
df = df.pivot(index=['index', 'Product'], columns='Category', values='value').reset_index()
df.columns.name = None
df = df.sort_values(by=['Product', 'Date'], ignore_index=True)
df = df.iloc[:, [2, 1, 3]]

# Display the final results
df
