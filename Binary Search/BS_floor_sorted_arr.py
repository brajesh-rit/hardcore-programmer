"""
https://practice.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1
Floor in a Sorted Array

Given a sorted array arr[] of size N without duplicates, and given a value x.
Floor of x is defined as the largest element K in arr[] such that K is smaller than or equal to x.
Find the index of K(0-based indexing).
Example 1:

Input:
N = 7, x = 0
arr[] = {1,2,8,10,11,12,19}
Output: -1
Explanation: No element less
than 0 is found. So output
is "-1".
Example 2:

Input:
N = 7, x = 5
arr[] = {1,2,8,10,11,12,19}
Output: 1
Explanation: Largest Number less than 5 is
2 (i.e K = 2), whose index is 1(0-based
indexing).
Your Task:
The task is to complete the function findFloor() which returns an integer denoting the index value of K or return -1 if there isn't any such number.

Expected Time Complexity: O(log N).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ N ≤ 107
1 ≤ arr[i] ≤ 1018
0 ≤ X ≤ arr[n-1]
"""

class Solution:
    def findFloor(self, arr, n, x):
        low = 0
        high = len(arr) - 1

        # If last element is smaller than x
        if x >= arr[high]:
            return high
        elif x < arr[low]:
            return -1

        while low <= high:
            mid = (high + low) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                result = mid
                low = mid + 1
            elif arr[mid] > x:
                high = mid - 1
        return result


# Your code here
arr = [1,2,8,10,11,12,19]
N = 7
x = 5

result = Solution()
print(result.findFloor(arr, N, x))