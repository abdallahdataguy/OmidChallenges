# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_excelchallenge-powerquerychallenge-excel-activity-7219445775007666177-Z81p/

# Create a function to generate 
# Z-scores given probabilities
def find_zscore(probability):
    diff = (df1 - probability).abs()
    indices = diff.stack().idxmin()
    return sum(indices)

# Read the data ranges
df1 = xl("B2:L13", headers=True)
df = xl("N2:N9", headers=True)

# Perform data munging
df1 = df1.set_index(keys='Z')   
df['Z'] = df['Probability'].map(find_zscore)

# Display the final results
df
