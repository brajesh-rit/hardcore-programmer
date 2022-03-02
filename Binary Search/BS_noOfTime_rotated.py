"""
https://www.geeksforgeeks.org/find-rotation-count-rotated-sorted-array/
Find the Rotation Count in Rotated Sorted array
Consider an array of distinct numbers sorted in increasing order.
The array has been rotated (clockwise) k number of times. Given such an array, find the value of k.
Examples:


Input : arr[] = {15, 18, 2, 3, 6, 12}
Output: 2
Explanation : Initial array must be {2, 3,
6, 12, 15, 18}. We get the given array after
rotating the initial array twice.

Input : arr[] = {7, 9, 11, 12, 5}
Output: 4

Input: arr[] = {7, 9, 11, 12, 15};
Output: 0
successful submit
"""
class Solution:
    def findKRotation(self, arr, n):
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

# Driver code
arr = [7, 9, 11, 12, 5]
#arr = [2,12,14,15,16,17]
#arr = [66,72,79,86,95,104, 106,110 ,119 ,123, 124 ,129 ,132 ,136, 137 ,142 ,150 ,2 ,12 ,14 ,17, 26, 30 ,36, 38, 46, 52 ,60]
n = len(arr)
result = Solution()
print(result.findKRotation(arr,n))