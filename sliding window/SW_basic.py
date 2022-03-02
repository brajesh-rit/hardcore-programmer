"""
https://practice.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1
Given an array of integers Arr of size N and a number K. Return the maximum sum of a subarray of size K.
Example 1:

Input:
N = 4, K = 2
Arr = [100, 200, 300, 400]
Output:
700
Explanation:
Arr3  + Arr4 =700,
which is maximum.
"""
class Solution:
    def maximumSumSubarray(self,k,arr,n):
        start = 0
        end = 0
        tot = 0
        ans = float('-inf')
        while end < n:
            tot += arr[end]
            # if (end-start+1) < k:
            #     end += 1
            if (end - start + 1) == k:
                ans = max(ans, tot)
                tot -= arr[start]
                start += 1
            end += 1
        return ans


test = Solution()
arr = [100, 200, 300, 400]
k = 2
n = len(arr)
print(test.maximumSumSubarray(k,arr,n))