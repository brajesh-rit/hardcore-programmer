class Solution:
    def minCoins(self, coins, m, v):
        #https://practice.geeksforgeeks.org/problems/number-of-coins1824/1#
        # create the matrix
        mem = [[-1 for x in range(v + 1)] for x in range(m + 1)]

        #initialize the base condition
        # row = inf  (we need some sum without any coin (array is empty) illogical but mathematically represent  infinite for this)
        # col = 0 (achieve sum= 0 for getting sum zero we need not take any coin)
        for row in range(m + 1):
            for col in range(v + 1):
                if col == 0:
                    mem[row][col] = 0
                elif row == 0:
                    mem[row][col] = float('inf')     

        #min_cnt = float('inf')
        for row in range(1,m+1):
            for col in range(1, v + 1):
                if coins[row -1 ] <= col:
                    mem[row][col] = min(1 + mem[row][col - coins[row - 1]] , mem[row - 1][col])
                else:
                    mem[row][col] = mem[row - 1][col]
        if mem[m][v] == float('inf'):
            return -1
        else:
            return mem[m][v]



# V = 30 #target sum from the given coin
# M = 3  #size of array
# coins = [25,10,5]
V = 4 #target sum from the given coin
M = 2  #size of array
coins = [15,1]

result = Solution()
print(result.minCoins(coins, M, V))