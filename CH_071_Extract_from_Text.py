# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_excelchallenge-powerquerychllenge-excel-activity-7210023687364780033-9mSa/

import pandas as pd
import re

# Read the Excel file
file_path = 'CH-071 Extract from Text.xlsx'
df = pd.read_excel(file_path, usecols='B', skiprows=1)

# Perform data wrangling
pattern = r'\b([.\w]+@[.\w]+[.][a-z]+)\b'
# Capture all emails, in case of multiple, join by ", "
emails = [', '.join(y) for x in df['Text'] if (y:=re.findall(pattern, x))]
# Split by ', " where multiple emails were captured
emails = [x for y in emails for x in y.split(', ')]
# Ensure unique emails while retaining the original capture order
emails = [x for i, x in enumerate(emails) if emails[ : i + 1].count(x) == 1]

df = pd.DataFrame(data=emails, columns=['Email Address'])

# Display the final dataset
df
