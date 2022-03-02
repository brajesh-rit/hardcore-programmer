#https://leetcode.com/problems/find-k-closest-elements/
#Given a (un)sorted integer array arr, two integers k and x, return the k closest integers to x in the array.
# The result should also be sorted in ascending order.

import heapq
class Solution(object):
    def findClosestElements(self, arr, k, x):
        res = []
        harr = []
        for i in range(len(arr)):
            heapq.heappush(harr,(arr[i] - x) * -1)
            if len(harr) > k:
                heapq.heappop(harr)
        for i in range(k):
            res.append((heapq.heappop(harr) * -1) + x)  # first multiple with -1 and then add x value otherwise wrong
        return sorted(res)

result = Solution()
arr = [1,1,1,10,10,10]
k = 1
x = 9
print(result.findClosestElements(arr,k,x))