# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_excelchallenge-powerquerychllenge-excel-activity-7214372344125870081-WYfl/

import pandas as pd

# Create a function to generate the required results
def char_based_rhombus(n):        
    left = list(range(1 if n % 2 else 2, n if n % 2 else n + 1, 2))
    right = list(range(n, 0 if n % 2 else 1, -2))
    items = left + right
    values =  [[''] * ((n - j) // 2) + ['*'] * j 
               + [''] * ((n - j) // 2)  for j in items]
    return values

# Perform data wrangling
df = pd.DataFrame(char_based_rhombus(20))

# Display the final output
df
