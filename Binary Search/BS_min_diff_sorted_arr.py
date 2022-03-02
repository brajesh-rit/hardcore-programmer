#Given a sorted array, find the element in the array which has minimum difference with the given number.
class Solution:
    def binary_search(self, arr, low, high, x):

        while low <= high:
            mid = (high + low) // 2
            if arr[mid] < x:
                low = mid + 1
            elif arr[mid] > x:
                high = mid - 1
            else:
                return mid
        if abs(arr[low] - x ) > abs(arr[high] - x ):
            return high
        else:
            return low

# Your code here
arr = [1,2,8,10,11,12,19]
N = 7
x = 13

result = Solution()
print(result.binary_search(arr, 0, N -1 , x))
