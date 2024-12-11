import numpy as np

# Creating a 2D array
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

print("Original 2D array:")
print(arr)

# Array shape
print("\nArray shape:", arr.shape)

# Accessing elements
print("\nAccessing specific elements:")
print("Element at position (1,2):", arr[1,2]) 
print("Element at position (2,3):", arr[2,3]) 

# Accessing all elements with their indices
print("\nAccessing all elements with indices:")
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        print(f"Element at ({i},{j}): {arr[i,j]}")

# Slicing
print("\nSlicing operations:")
print("First two rows:")
print(arr[0:2])  # First two rows

print("\nAll rows, columns 1 to 3:")
print(arr[:, 1:4])  # All rows, columns 1 to 3

print("\nSlice from row 1 to end, columns 2 to end:")
print(arr[1:, 2:])  # From row 1 to end, columns 2 to end


