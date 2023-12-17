# Find the correlation between the first and second columns
correlation = df[0].corr(df[1])

# Print the correlation coefficient
print(correlation)

# Find the covariance between the second and third columns
covariance = df[1].cov(df[2])

# Print the covariance
print(covariance)
