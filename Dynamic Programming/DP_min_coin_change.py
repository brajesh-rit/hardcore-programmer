"""
https://practice.geeksforgeeks.org/problems/number-of-coins1824/1
Given a value V and array coins[] of size M, the task is to make the change for V cents,
given that you have an infinite supply of each of coins{coins1, coins2, ..., coinsm} valued coins.
Find the minimum number of coins to make the change. If not possible to make change then return -1.

Example 1:

Input: V = 30, M = 3, coins[] = {25, 10, 5}
Output: 2
Explanation: Use one 25 cent coin
and one 5 cent coin
"""

class Solution:
    def minCoins1(self, coins, m, v):
        if v == 0:
            return 0
        min_count = float('inf')
        # Try every coin that has smaller or equal value than V
        for i in range(m):
            if coins[i] <= v:
                tmp = self.minCoins(coins,m,v-coins[i]) + 1
                min_count = min(min_count , tmp)

        return min_count

    def minCoins(self, coins, m, v):
        def solve (coins, m, v):
            min_arr = [float('inf') for _ in range(v+1)]
            #base condition
            min_arr[0] = 0
            for col in range(v+1):
                # Try every coin that has smaller or equal value than V
                for i in range(m):
                    if coins[i] <= col:
                        tmp = min_arr[col-coins[i]] + 1
                        min_arr[col] = min(min_arr[col] , tmp)

            return min_arr[v]
        res = solve(coins,m,v)
        if res == float('inf'):
            return -1
        else:
            return res


test = Solution()
# coins = [9, 6, 5, 1]
# V = 11
coins = [15, 4]
V = 2
m = len(coins)
print("Minimum coins required is", test.minCoins(coins, m, V))