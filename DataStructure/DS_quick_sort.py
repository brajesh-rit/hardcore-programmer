# This function takes first element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr,low,high):
    pivot = arr[low]
    i , j = low , high - 1

    while (i < j):
        while arr[i] <= pivot:
            i+= 1
        while arr[j] > pivot:
            j -= 1
        if (i < j):
            arr[i], arr[j] = arr[j] , arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j

def quickSort(arr,l,h):
    if l < h:
        j = partition(arr, l,h)
        quickSort(arr, l, j)
        quickSort(arr, j+1, h)

arr =[10,16,8,12,15,6,3,9,5]
high = len(arr)                # send high always more than one of correct length
low = 0
quickSort(arr, low, high)
print(arr)