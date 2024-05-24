# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_excelchallenge-powerquerychllenge-excel-activity-7193353862840225792-SDP0/

import pandas as pd

# Read the Excel file
file_path = 'CH-048 Transformation.xlsx'
df = pd.read_excel(file_path, usecols='B')

# Perform data transformation and cleansing
c = df.columns[0]
models1 = df[c].apply(lambda x: x[ :x.find('+')]).unique()
models2 = df[c].apply(lambda x: x[x.find('+') + 1: ]).unique()
models  = list(models1) + [x for x in models2 if x not in models1]

values = []
for i in models:
    value = []
    for j in models:   
        if i == j:
            value.append('')
        else:
            value.append(df[c].apply(lambda x: (i in x.split('+')) & (j in x.split('+'))).sum())
    values.append(value)

df = pd.DataFrame(values, columns=models, index=models)
df = df.astype(str).replace('0', '')

# Display final results
df
