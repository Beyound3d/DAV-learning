import numpy as np

# Get the user input for the dimensions of the array
m = int(input("Enter the value for m: "))
n = int(input("Enter the value for n: "))

# Create a 2-dimensional array of size m x n integer elements
A = np.random.randint(10, 100, (m, n))

# Print the shape, type and data type of the array
print("Shape of the array:", A.shape)
print("Type of the array:", type(A))
print("Data type of the array:", A.dtype)

# Reshape the array into n x m
A_reshaped = np.reshape(A, (n, m))

# Print the shape of the reshaped array
print("Shape of the reshaped array:", A_reshaped.shape)
