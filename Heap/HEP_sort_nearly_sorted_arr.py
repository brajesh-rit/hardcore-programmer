"""
https://practice.geeksforgeeks.org/problems/nearly-sorted-algorithm/0
Given an array of n elements, where each element is at most k away from its target position.
The task is to print array in sorted form.
"""

import heapq
import sys
class Solution:
    def kNearlySort(self, arr, k):
        val = []
        res = []
        for i in range(len(arr)):
            heapq.heappush(val,arr[i])
            if len(val) > k:
                res.append(heapq.heappop(val))
        for i in range(k):
            res.append(heapq.heappop(val))
        return res


k = 3
arr = [2, 6, 3, 12, 56, 8]
res = Solution()
print(res.kNearlySort(arr,k))