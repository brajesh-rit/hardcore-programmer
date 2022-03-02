#https://leetcode.com/problems/minimum-cost-to-merge-stones/
# above problem is DP problem
#https://www.geeksforgeeks.org/optimal-file-merge-patterns/
#There are given n ropes of different lengths, we need to connect these ropes into one rope.
# The cost to connect two ropes is equal to sum of their lengths. We need to connect the ropes with minimum cost.

import heapq
class Solution:
    def optimalMerge(self, arr):
        harr = []
        for i in range(len(arr)):
            heapq.heappush(harr,arr[i])
        Tcost = 0
        while len(harr) >= 2 :
            cost = heapq.heappop(harr) + heapq.heappop(harr)
            heapq.heappush(harr,cost)
            Tcost = Tcost + cost
        return Tcost

result = Solution()
arr = [2, 3, 4, 5, 6, 7]
print(result.optimalMerge(arr))
