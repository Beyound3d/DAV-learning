import numpy as np

# Create a random integer array
B = np.random.randint(10, 100, 10)

# Get the indices of the sorted elements
sorted_indices = np.argsort(B)

# Print the sorted indices
print(sorted_indices)

