import numpy as np

# Create a random array
A = np.random.rand(10)

# Create three arrays to store the indices of zero, non-zero and NaN elements
zero_indices = []
non_zero_indices = []
nan_indices = []

# Iterate over the array and record the indices of the elements in the respective arrays
for i in range(len(A)):
    if A[i] == 0:
        zero_indices.append(i)
    elif np.isnan(A[i]):
        nan_indices.append(i)
    else:
        non_zero_indices.append(i)

# Print the indices of the zero, non-zero and NaN elements
