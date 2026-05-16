import numpy as np

# Dataset
np.random.seed(42)
data_array = np.random.randint(1, 501, size=(10, 10))

print("Original Array:\n")
print(data_array)

# 1. Find global mean and replace elements greater than mean with 0
global_mean = np.mean(data_array)

modified_array = np.where(data_array > global_mean, 0, data_array)

print("\nGlobal Mean:", global_mean)

print("\nModified Array (values > mean replaced with 0):\n")
print(modified_array)

# 2. Column sums and row standard deviations
column_sums = np.sum(modified_array, axis=0)
row_std = np.std(modified_array, axis=1)

print("\nSum of Each Column:\n")
print(column_sums)

print("\nStandard Deviation of Each Row:\n")
print(row_std)

# 3. Extract center 4x4 sub-matrix and flatten to 1D array
center_submatrix = modified_array[3:7, 3:7]

flat_array = center_submatrix.flatten()

print("\nCenter 4x4 Sub-Matrix:\n")
print(center_submatrix)

print("\nFlattened 1D Array:\n")
print(flat_array)