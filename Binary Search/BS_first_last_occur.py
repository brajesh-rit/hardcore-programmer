#https://practice.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/1
#Given a sorted array arr containing n elements with possibly duplicate elements,
# the task is to find indexes of first and last occurrences of an element x in the given array.
def find(arr,n,x):
    def first(arr,x):
        low = 0
        high = len(arr) - 1
        mid = 0
        res = -1
        while low <= high:

            mid = (high + low) // 2

            if arr[mid] < x:
                low = mid + 1

            elif arr[mid] > x:
                high = mid - 1

            else:
                res =  mid
                high =  mid -1  # above two line is change here if you want first occurence

        return res

    def last(arr, x):
        low = 0
        high = len(arr) - 1
        mid = 0
        res = -1
        while low <= high:

            mid = (high + low) // 2

            if arr[mid] < x:
                low = mid + 1

            elif arr[mid] > x:
                high = mid - 1

            else:
                res = mid
                low = mid + 1  # above two line is change here if you want last occurence
        return res

    Fval = first(arr,x)
    lval = last(arr,x)
    return [Fval,lval]

n = 9
x = 5
arr = [1, 3, 5, 5, 5, 5, 7, 123, 125 ]
print(find(arr,n,x))