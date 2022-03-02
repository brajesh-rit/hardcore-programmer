"""
https://leetcode.com/problems/search-in-rotated-sorted-array/
FIND AN ELEMENT IN A ROTATED SORTED ARRAY:

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
"""
class Solution(object):
    def binary_search(self,arr, low, high, x):
        while low <= high:
            mid = (high + low) // 2
            if arr[mid] < x:
                low = mid + 1
            elif arr[mid] > x:
                high = mid - 1
            else:
                return mid
        return -1
    def find_min(self, arr):
        n = len(arr)
        start = 0
        end = n - 1
        while start <= end:
            mid = start + (end - start) // 2
            prev = (mid - 1 + n) % n
            nex = (mid + 1) % n
            if arr[start] <= arr[end]:
                return start
            elif arr[mid] < arr[prev] and arr[mid] <= arr[nex]:
                return mid
            elif arr[mid] >= arr[start]:
                start = mid + 1
            elif arr[mid] <= arr[end]:
                end = mid - 1
            else:
                return 0

    def search(self, nums, target):
        min_index = self.find_min(nums)
        # if min value itself is target then return same index becuase we ignore this value in binary search
        if nums[min_index] == target:
            return min_index
        low = 0
        high = len(nums) - 1
        result = -1
        if low < min_index:
            result = self.binary_search(nums,low, min_index - 1, target)
        if result == -1:
            result = self.binary_search(nums, min_index + 1, high, target)
        return result

#nums = [4,5,6,7,0,1,2]
#nums = [1]
nums = [1,3]
target = 3
result = Solution()
print(result.search(nums,target))