def binary_search_desc(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = low + (high - low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            high = mid - 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            low = mid + 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1

def binary_search_asc(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1

# Test array
arr = [2, 3, 4, 10, 40]
x = 10

if len(arr) == 1:
    if x == arr[1]:
        print("Element is present at index", str(1))
    else:
        print('Not found')
else:
    if arr[2] > arr[1]:
        result = binary_search_asc(arr,x)
    else:
        result = binary_search_desc(arr, x)


if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")