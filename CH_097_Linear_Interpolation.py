# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_powerabrquery-excel-powerabrqueryabrtips-activity-7229230243260022785-HRQe/

# read the data range
df = xl("B2:E5", headers=True)

# Perform data manipulation
df2 = pd.DataFrame(data=range(2010, 2023), columns=['Year'])
df = pd.merge(df2, df, how='left', on='Year')
df = df.interpolate(method='linear')
n = len(df)

df.loc[0] = 2 * df.loc[1] - df.loc[2]
df.loc[n-1] = 2 * df.loc[n-2] - df.loc[n-3]

# Display the final results
df
