import numpy as np
import pandas as pd

# Generate a random dataframe
df = pd.DataFrame(np.random.rand(50, 3))

# Replace 10% of the values by null values
num_null_values = int(0.1 * df.size)
null_indices = np.random.choice(df.size, num_null_values, replace=False)
df.iloc[null_indices] = np.nan

# Print the dataframe
print(df)
