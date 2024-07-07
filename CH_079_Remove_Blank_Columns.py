# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_excelchallenge-powerquerychallenge-excel-activity-7215821890907459585-Pekp/

# Read the data range
df = xl("B2:I6", headers=True)

# Drop columns if entirely blank
df = df.dropna(how='all', axis=1)

# Display the final dataset
df
