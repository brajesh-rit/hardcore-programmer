class Solution:
    # Function to find length of shortest common supersequence of two strings.
    def shortestCommonSupersequence(self, X, Y, m, n):
        mem = [[-1 for x in range(n + 1)] for x in range(m + 1)]

        for row in range(m + 1):
            for col in range(n + 1):
                if row == 0 or col == 0:
                    mem[row][col] = 0

        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if X[row - 1] == Y[col - 1]:
                    mem[row][col] = 1 + mem[row - 1][col - 1]
                else:
                    mem[row][col] = max(mem[row - 1][col], mem[row][col - 1])

        output = m + n - mem[m][n]
        return output

m = 4
n = 4
X = 'abcd'
Y = 'xycd'
result = Solution()
print(result.shortestCommonSupersequence(X, Y ,m ,n))