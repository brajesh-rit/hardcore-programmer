class Solution:
    def cutRod(self, price, n):
        # if property of rod is not given then create yourself here it to property (length and price)
        rodLen = list(range(1,n+1))               # list in-line function convert the range of number to list
        mem = [[-1 for x in range(n+1)] for x in range(n+1)]

        #base condition
        for row in range(n + 1):
            for col in range(n+1):
                if col == 0:
                    mem[row][col] = 0
                elif row == 0:
                    mem[row][col] = 0

        for row in range(1,n+1):
            for col in range(1,n+1):
                if rodLen[row - 1] <= col:
                    mem[row][col] = max(price[row-1] + mem[row ][col - rodLen[row - 1] ], mem[row - 1][col])    # unbounded  variation here mem[row][col - rodLen[row - 1]] instead of mem[row -1][col - rodLen[row - 1]]
                else:
                    mem[row][col] = mem[row - 1][col]

        return mem[n][n]

price =  [1, 5, 8, 9, 10, 17, 17, 20]
n = 8
result = Solution()
print(result.cutRod(price,n))
