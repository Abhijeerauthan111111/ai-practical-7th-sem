def linear_search(arr, target):
    """
    Perform linear search to find target element in array
    Returns index if found, -1 if not found
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# usage
if __name__ == "__main__":
    
    # Initialize array of size 10
    arr = [0] * 10

    # Get input from user
    print("Enter 10 numbers:")
    for i in range(10):
        arr[i] = int(input(f"Enter number {i+1}: "))

    # Get search element
    search_element = int(input("Enter number to search: "))

    # Perform linear search
    result = linear_search(arr, search_element)

    # Print results
    if result != -1:
        print(f"Element {search_element} found at index {result}")
    else:
        print(f"Element {search_element} not found in array")