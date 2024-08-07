# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_excelchallenge-powerquerychallenge-excel-activity-7217996213822926849-XoCm/

# Read the data range
df = xl("B2:D7", headers=True)

# Perform data wrangling
df['Date'] = df.apply(
lambda x: pd.date_range(x['From'], x['To']), axis=1
)
df = df.explode(column='Date', ignore_index=True)
df = df.groupby('Date')['Supervisor'].agg(', '.join).reset_index()
df.columns = ['Date', 'Supervisors']

# Display the final results
df
