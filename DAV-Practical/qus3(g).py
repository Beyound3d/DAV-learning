# Compute the IQR
iqr = df[1].quantile(0.75) - df[1].quantile(0.25)

# Detect outliers
outliers = df[1] < (df[1].quantile(0.25) - 1.5 * iqr) | df[1] > (df[1].quantile(0.75) + 1.5 * iqr)

# Drop the rows having outliers
df.drop(df.index[outliers], inplace=True)

# Print the dataframe
print(df)
