# Discretize the second column and create 5 bins
binned_column = pd.cut(df[1], bins=5)

# Print the binned column
print(binned_column)

# We can also specify the bin edges instead of the number of bins. For example, to create 5 bins with equal intervals of 0.1, we can use the following code:

# Discretize the second column and create 5 bins with equal intervals of 0.1

bin_edges = np.arange(0.4, 0.9, 0.1)
binned_column = pd.cut(df[1], bins=bin_edges)

# Print the binned column
print(binned_column)
