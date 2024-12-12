import numpy as np  #pip install numpy or pip install --user numpy

# Creating a 1D array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Original 1D array:")
print(arr)

# Array shape
print("\nShape of array:", arr.shape)

# Accessing elements
print("\nAccessing elements:")
print("First element:", arr[0])
print("Last element:", arr[-1])
print("Third element:", arr[2])

# Accessing all elements with their indices
print("\nAccessing all elements with their indices:")
for i in range(arr.size):
    print(f"Element at index {i}: {arr[i]}")

# Slicing operations
print("\nSlicing operations:")
print("First three elements:", arr[0:3])
print("Elements from index 4 to 7:", arr[4:8])
print("Every second element:", arr[::2])
print("Reverse array:", arr[::-1])
print("Elements from 3rd to 7th position:", arr[2:7])
