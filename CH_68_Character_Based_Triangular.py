# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_excelchallenge-powerquerychllenge-excel-activity-7207849349693775872-m8JA/

import pandas as pd

# Create a function to generate the required results
def triangular(n):
    items = range(n, 0, -2)
    values =  {i: [''] * i + ['*'] * items[i] + [''] * i 
               for i in range(len(items))}
    return values

# Perform data wrangling
df = pd.DataFrame(triangular(11))

# Display the final output
df
