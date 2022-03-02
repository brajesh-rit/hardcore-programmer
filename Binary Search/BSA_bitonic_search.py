"""
https://www.geeksforgeeks.org/find-element-bitonic-array/
Find an element in Bitonic array
Given a bitonic sequence of n distinct elements, write a program to find a given element x in the bitonic 
sequence in O(log n) time. A Bitonic Sequence is a sequence of numbers that is first strictly
 increasing then after a point strictly decreasing.

Examples:
Input :  arr[] = {-3, 9, 18, 20, 17, 5, 1};
         key = 20
Output : Found at index 3

Input :  arr[] = {5, 6, 7, 8, 9, 10, 3, 2, 1};
         key = 30
Output : Not Found
"""

class Solution(object):
    def ascendingBinarySearch(self, arr, low, high, key):

        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] == key:
                return mid

            if arr[mid] > key:
                high = mid - 1
            else:
                low = mid + 1

        return -1

    def descendingBinarySearch(self, arr, low, high, key):

        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] == key:
                return mid

            if arr[mid] < key:
                high = mid - 1
            else:
                low = mid + 1

        return -1

    def findPeakElement(self, nums):
        start = 0
        end = len(nums)-1
        while start < end:
            mid = start + (end -  start) // 2  # to avoid integer overflow
            if nums[mid] > nums[mid+1]:
                end = mid
            else:
                start = mid+1
        return start

    def searchBitonic(self, arr, n, key, index):

        if key > arr[index]:
            return -1
        elif key == arr[index]:
            return index
        else:
            temp = self.ascendingBinarySearch(arr, 0, index - 1, key)
            if temp != -1:
                return temp

            # search in right of k
            return self.descendingBinarySearch(arr, index + 1, n - 1, key)


arr = [-8, 1, 2, 3, 4, 5, -2, -3]
key = 1
n = len(arr)
l = 0
r = n - 1

result = Solution()

# Function call
index = result.findPeakElement(arr)

x = result.searchBitonic(arr, n, key, index)

if x == -1:
    print("Element Not Found")
else:
    print("Element Found at index", x)