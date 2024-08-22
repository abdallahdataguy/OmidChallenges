# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_powerabrquery-excel-powerabrqueryabrtips-activity-7232129349246722048-j_1F/

from itertools import combinations

# Read the data range
df = xl("B2:C7", headers=True)

# Perform data munging
values = []
for comb in combinations(df['ID'], 3):
    str_comb = ','.join(str(x) for x in comb)
    total = sum(
        df['value (cost)'][df['ID'] == x].values[0] for x in comb
    )
    values.append([str_comb, total])

df = pd.DataFrame(
    data=values, 
    columns=['ID Combination', 'Total value (cost)']
)

# Display the final results
df
