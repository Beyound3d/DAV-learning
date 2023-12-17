# Identify missing values
missing_values = df.isnull()

# Count missing values
count_missing_values = missing_values.sum()

# Print the count of missing values
print(count_missing_values)
