# Link to the challenge
# https://www.linkedin.com/posts/omid-motamedisedeh-74aba166_excelchallenge-powerquerychllenge-excel-activity-7210748457702105088-ODIC/

import pandas as pd

# Function to generate a list of the first n Fibonacci numbers
def fibonacci_sequence(n):
    def fibonacci(n, memo={}):
        if n in memo:
            return memo[n]
        if n <= 1:
            return n
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        return memo[n]
    return [fibonacci(i) for i in range(n)]

# Perform data wrangling
df = pd.DataFrame(fibonacci_sequence(18), columns=['Fibonacci Sequence'])

# Display the final dataset
df
