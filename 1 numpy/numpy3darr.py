import numpy as np

# Create a 3D array (2 matrices with 3 rows and 4 columns each)
arr_3d = np.array([
    [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]],
    
    [[13, 14, 15, 16],
     [17, 18, 19, 20],
     [21, 22, 23, 24]]
])

print("Original 3D Array:")
print(arr_3d)
print("\nShape of array:", arr_3d.shape)

# Accessing elements
print("\nAccessing specific elements:")
print("Element at (0,0,0):", arr_3d[0,0,0])  # First element
print("Element at (1,2,3):", arr_3d[1,2,3])  # Last element
# Iterating through all elements with their indices
for i in range(arr_3d.shape[0]):
    for j in range(arr_3d.shape[1]):
        for k in range(arr_3d.shape[2]):
            print(f"arr_3d[{i},{j},{k}] = {arr_3d[i,j,k]}")

# Slicing operations
print("\nSlicing operations:")
# Get first matrix
print("\nFirst matrix:")
print(arr_3d[0])

# Get first row of second matrix
print("\nFirst row of second matrix:")
print(arr_3d[1,0])

# Get all elements from index 1 to 3 in each row
print("\nElements from index 1 to 3 in each row:")
print(arr_3d[:,:,1:3])
