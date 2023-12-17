# Remove all duplicates from the first column
df = df.drop_duplicates(subset=[0])

# Print the dataframe
print(df)
