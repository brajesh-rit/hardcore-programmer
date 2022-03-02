"""
https://www.geeksforgeeks.org/ceiling-in-a-sorted-array/
Ceiling in a sorted array

Given a sorted array and a value x, the ceiling of x is the smallest element in array greater than or equal to x,
and the floor is the greatest element smaller than or equal to x.
Assume than the array is sorted in non-decreasing order. Write efficient functions to find floor and ceiling of x.
Examples :


For example, let the input array be {1, 2, 8, 10, 10, 12, 19}
For x = 0:    floor doesn't exist in array,  ceil  = 1
For x = 1:    floor  = 1,  ceil  = 1
For x = 5:    floor  = 2,  ceil  = 8
For x = 20:   floor  = 19,  ceil doesn't exist in array
In below methods, we have implemented only ceiling search functions. Floor search can be implemented in the same way.
"""

#https://www.geeksforgeeks.org/ceiling-in-a-sorted-array/
class Solution:
    def ceilSearch(self, arr, n, x):
        low = 0
        high = len(arr) - 1

        # If last element is smaller than x
        if x > arr[high]:
            return -1
        elif x <= arr[low]:
            return low

        while low <= high:
            mid = (high + low) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                low = mid + 1
            elif arr[mid] > x:
                result = mid
                high = mid - 1
        return result


# Your code here
arr = [1,2,8,10,11,12,19]
N = 7
x = 3

result = Solution()
print(result.ceilSearch(arr, N, x))