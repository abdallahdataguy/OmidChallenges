# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_excelchallenge-powerquerychallenge-excel-activity-7218720996646608897-Otox/

# Read the data range
rng = xl("B3")

# Perform data wrangling
values = [x.split(", ") for x in rng.split(";")]
df = pd.DataFrame(
    data=values, 
    columns=['Date', 'Product', 'Quantity']
)
# Display the final results
df
