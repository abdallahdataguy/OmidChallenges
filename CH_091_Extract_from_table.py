# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_excelchallenge-powerquerychllenge-excel-activity-7224519224495329281-Leg1/

# Read the data range
df1 = xl("B2:E6", headers=True)

# Perform data munging
df1 = df1.melt(id_vars=['Branch NO'], value_vars=df1.columns[1:], var_name='Department', value_name='Name')
df1['Branch NO'] = 'Branch ' + df1['Branch NO'].map(str)
df1['Value'] = '\u2713'
df = df1.pivot(index=['Name', 'Department'], columns='Branch NO', values='Value').reset_index().fillna('')
df = df.sort_values(by='Name', key=lambda x: [df1.Name.tolist().index(x) for x in df.Name], ignore_index=True)
df.columns.name = ''

# Display the final results
df
