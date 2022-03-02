"""
https://leetcode.com/problems/minimum-cost-to-merge-stones/
There are n piles of stones arranged in a row. The ith pile has stones[i] stones.

A move consists of merging exactly k consecutive piles into one pile, and the cost of this move is equal to the total number of stones in these k piles.

Return the minimum cost to merge all piles of stones into one pile. If it is impossible, return -1.



Example 1:

Input: stones = [3,2,4,1], k = 2
Output: 20
Explanation: We start with [3, 2, 4, 1].
We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
We merge [4, 1] for a cost of 5, and we are left with [5, 5].
We merge [5, 5] for a cost of 10, and we are left with [10].
The total cost was 20, and this is the minimum possible.
Example 2:

Input: stones = [3,2,4,1], k = 3
Output: -1
Explanation: After any merge operation, there are 2 piles left, and we can't merge anymore.  So the task is impossible.
Example 3:

Input: stones = [3,5,1,2,6], k = 3
Output: 25
Explanation: We start with [3, 5, 1, 2, 6].
We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
We merge [3, 8, 6] for a cost of 17, and we are left with [17].
The total cost was 25, and this is the minimum possible.
@@@@@@@@@@@@@@@@@@@@@@@@@@@
Below solution works when consecutive word remove from the question.
otherwise it is DP problem
TODO
work on DP way
read on what is functools.lru_cache?
"""
import heapq
class Solution(object):
    def mergeStones1(self, arr, k):
        harr = []
        for i in range(len(arr)):
            heapq.heappush(harr, arr[i])
        Tcost = 0
        while len(harr) >= k:
            cost = 0
            for i in range(k):
                cost = cost + heapq.heappop(harr)
            heapq.heappush(harr, cost)
            Tcost = Tcost + cost
        else:
            if len(harr) > 1:
                return -1
        return Tcost

    def mergeStones(self, stones, K):
        n = len(stones)
        inf = float('inf')
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        import functools

        @functools.lru_cache(None)
        def dp(i, j, m):
            if (j - i + 1 - m) % (K - 1):
                return inf
            if i == j:
                return 0 if m == 1 else inf
            if m == 1:
                return dp(i, j, K) + prefix[j + 1] - prefix[i]
            return min(dp(i, mid, 1) + dp(mid + 1, j, m - 1) for mid in range(i, j, K - 1))

        res = dp(0, n - 1, 1)
        return res if res < inf else -1


stones = [3,2,4,1]
k = 2
test = Solution()
print(test.mergeStones(stones,k))

stones = [3,5,1,2,6]
k = 3
test = Solution()
print(test.mergeStones(stones,k))