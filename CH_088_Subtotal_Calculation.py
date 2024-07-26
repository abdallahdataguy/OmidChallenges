# Python in Excel

# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_excelchallenge-powerquerychallenge-excel-activity-7222344872421122048-dusD/

import pandas as pd

# Read the data range
df = xl("B2:E18", headers=True)

# Perform data munging
grand_total = ['Grand Total', '', df['Region 1'].sum(), df['Region 2'].sum()]
dfs = []
for product in df['Product'].unique():
    dfn = df[df['Product'] == product].reset_index(drop=True)
    dfn.loc[len(dfn)] = ['Total ' + product, '', dfn['Region 1'].sum(), dfn['Region 2'].sum()]
    dfs.append(dfn)

df = pd.concat(dfs).reset_index(drop=True)
df.loc[len(df)] = grand_total   
df['Total Regions'] = df['Region 1'] + df['Region 2']

# Display the final results
df
