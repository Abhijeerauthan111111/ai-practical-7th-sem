import numpy as np

# Create a 3D array (2 matrice with 3 rows and 4 columns each)
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
