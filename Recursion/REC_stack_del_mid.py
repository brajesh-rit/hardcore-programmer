#Delete Middle Element of a Stack Using Recursion.

def solve(arr, k):
    if k == 1:
        arr.pop()
        return
    val = arr.pop()
    solve(arr, k-1)
    arr.append(val)
    return
arr = [5,4,3,2,1]
n = len(arr)
k = int(n/2) + 1
solve(arr,k)
print(arr)