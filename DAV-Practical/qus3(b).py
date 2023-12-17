# Drop the column having more than 5 null values
df = df.dropna(axis='columns', thresh=5)

# Print the dataframe
print(df)
