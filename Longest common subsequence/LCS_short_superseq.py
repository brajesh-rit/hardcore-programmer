"""
https://www.geeksforgeeks.org/print-shortest-common-supersequence/
Given two strings X and Y, print the shortest string that has both X and Y as subsequences. If multiple shortest supersequence exists, print any one of them.
Examples:


Input: X = "AGGTAB",  Y = "GXTXAYB"
Output: "AGXGTXAYB" OR "AGGXTXAYB"
OR Any string that represents shortest
supersequence of X and Y
"""

class Solution:
    def lcsPrintSuper(self, s1, s2, m, n):
        mem = [[-1 for _ in range(n+1)] for _ in range(m+1)]

        for row in range(m+1):
            for col in range(n+1):
                if row == 0 or col == 0:
                    mem[row][col] = 0

        for row in range(1,m+1):
            for col in range(1,n+1):
                if s1[row-1] == s2[col-1]:
                    mem[row][col] = mem[row-1][col-1] + 1
                else:
                    mem[row][col] = max(mem[row - 1][col] , mem[row][col-1])
        row = m
        col = n
        res = ""
        while row > 0 and col > 0:
                if s1[row-1] == s2[col-1]:
                    res = res + s1[row - 1]
                    row -= 1
                    col -= 1
                else:
                    if mem[row - 1][col] >=  mem[row][col-1]:
                        res = res + s1[row-1]
                        row -= 1
                    else:
                        res = res + s2[col-1]
                        col -= 1
        while row > 0:
            res += s1[row-1]
            row -= 1
        while col > 0:
            res += s2[col-1]
            col -= 1
        res = res[::-1]
        return res

X = "AGGTAB"
Y = "GXTXAYB"
m = len(X)
n = len(Y)
test = Solution()
print(test.lcsPrintSuper(X,Y,m,n))