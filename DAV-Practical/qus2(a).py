import numpy as np

# Generate a random integer array
A = np.random.randint(10, 100, (10, 5))

# Compute the mean, standard deviation, and variance along the second axis
mean = np.mean(A, axis=1)
std = np.std(A, axis=1)
var = np.var(A, axis=1)

# Print the results
print("Mean:", mean)
print("Standard deviation:", std)
print("Variance:", var)
