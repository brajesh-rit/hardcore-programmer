"""
https://www.geeksforgeeks.org/printing-longest-common-subsequence/
Given two sequences, print the longest subsequence present in both of them.

Examples:
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
"""
class Solution:
    def lcsPrint(self, s1, s2, m, n):
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
        while row > 0 or col > 0:
                if s1[row-1] == s2[col-1]:
                    res = res + s1[row - 1]
                    row -= 1
                    col -= 1
                else:
                    if mem[row - 1][col] > mem[row][col-1]:
                        row -= 1
                    else:
                        col -= 1
        res = res[::-1]
        return res


x = 6
y = 6
s1 = 'ABCDGH'
s2 = 'ACDGHR'
result = Solution()
print(result.lcsPrint( s1, s2, x, y))