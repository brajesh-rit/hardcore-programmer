"""
Problem Description:

Given an array containing N positive integers and an integer K. Your task is to find the length of the longest Sub-Array with sum of the elements equal to the given value K.

For Input:
1
7 5
4 1 1 1 2 3 5
your output is:
4
"""
class Solution:
    def lenOfLongSubarr1 (self, nums, n, k):
        leng = n
        start = 0
        end = 0
        tot = 0
        ans = float('-inf')
        while end < leng:
            tot += nums[end]
            if tot < k:
               None
            elif tot == k:
                ans = max(ans, (end - start + 1))
            elif tot > k:
                while tot > k:
                    tot -= nums[start]
                    start += 1
            end += 1
        return ans

test = Solution()
nums = [4, 1, 1, 1, 2, 3, 5]
n = len(nums)
k = 5
print(test.lenOfLongSubarr1(nums,n,k))