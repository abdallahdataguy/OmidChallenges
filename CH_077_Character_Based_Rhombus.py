# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_excelchallenge-powerquerychllenge-excel-activity-7214372344125870081-WYfl/

import pandas as pd

# Create a function to generate the required results
def char_based_rhombus(n):
    left = list(range(1, n, 2))
    right = list(range(n if n % 2 else n - 1, 0, -2))
    items = left + right
    values =  {i: [''] * ((n - j) // 2) + ['*'] * j 
               + [''] * ((n - j) // 2)  
               for i, j in enumerate(items)}
    return values

# Perform data wrangling
df = pd.DataFrame(char_based_rhombus(14))

# Display the final output
df
