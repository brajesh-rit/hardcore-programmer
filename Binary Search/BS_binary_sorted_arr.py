"""
https://www.geeksforgeeks.org/find-index-first-1-infinite-sorted-array-0s-1s/
Given an infinite sorted array consisting 0s and 1s. The problem is to find the index of first ‘1’ in that array.
As the array is infinite, therefore it is guaranteed that number ‘1’ will be present in the array.
Examples:


Input : arr[] = {0, 0, 1, 1, 1, 1}
Output : 2

Input : arr[] = {1, 1, 1, 1,, 1, 1}
Output : 0
"""

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
        return -1

    def findPos(self, arr, key):

        low, high, val = 0, 1, arr[0]
        while val < key:
            low = high  # store previous high
            high = 2 * high  # double high index
            val = arr[high]  # update new val

        # at this point we have updated low and high indices,
        # thus use binary search between them
        return self.binary_search(arr, low, high, key)

arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
key = 1
test = Solution()
print(test.findPos(arr,key))