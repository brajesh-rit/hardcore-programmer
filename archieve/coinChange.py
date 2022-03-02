class Solution:
    def count(self, S, m, n):
        mem = [[-1 for x in range(n + 1)] for x in range(m + 1)]
        for row in range(m + 1):
            for col in range(n +  1):
                if col == 0:
                    mem[row][col] = 1
                elif row == 0:
                    mem[row][col] = 0
        for row in range(1,m + 1):
            for col in range(1,n + 1):
                if S[row -1] <= col:
                    mem[row][col] = mem[row ][col - S[row - 1]] + mem[row - 1][col]
                else:
                    mem[row][col] = mem[row - 1][col]

        return mem[m][n]

n = 4 # target sum from the given coin
m = 3 # size of the array
S = [1, 2, 3]  #array of the
result = Solution()
print(result.count(S,m,n))
