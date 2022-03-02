"""
https://practice.geeksforgeeks.org/problems/subset-sum-problem2014/1
Given an array arr[] of size N, check if it can be partitioned into two parts
such that the sum of elements in both parts is the same.

Example 1:

Input: N = 4
arr = {1, 5, 11, 5}
Output: YES
Explaination:
The two parts are {1, 5, 5} and {11}.
"""
class Solution:
    def equalPartition(self, N, arr):
        def solve(arr, n, tot):
            if n== 0 and tot > 0:
                return False
            if tot == 0:
                return True
            if arr[n-1] > tot:
                return  solve(arr , n-1 ,tot)
            else:
                return solve(arr, n-1,tot) or solve(arr, n-1, tot- arr[n-1])

        tot = sum(arr)
        if tot% 2 != 0:
            return False
        tot = int(tot/2)
        return solve(arr, N ,tot)


arr = [5, 6, 6, 5, 7, 4, 7, 6]
N = 4
test = Solution()
print(test.equalPartition(N,arr))