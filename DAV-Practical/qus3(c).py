# Compute the sum of all values in each row
row_sums = df.sum(axis=1)

# Get the index of the row with the maximum sum
max_row_index = row_sums.idxmax()

# Drop the row with the maximum sum
df.drop(max_row_index, inplace=True
