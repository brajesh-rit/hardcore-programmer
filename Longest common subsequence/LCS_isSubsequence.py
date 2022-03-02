#https://leetcode.com/problems/is-subsequence/
#A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
#  of the characters without disturbing the relative positions of the remaining characters.
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

class Solution(object):
    def isSubsequence(self, s, t):
        sLen = len(s)
        tLen = len(t)
        if sLen == 0:
            return  True
        elif tLen == 0:
            return  False
        mem = [[-1 for x in range(tLen + 1)] for x in range(sLen + 1)]

        for row in range(sLen + 1):
            for col in range(tLen + 1):
                if row == 0 or col == 0:
                    mem[row][col] = 0

        for row in range(1,sLen + 1):
            for col in range(1, tLen + 1):
                if s[row - 1] == t[col - 1]:
                    mem[row][col] = 1+ mem[row -1][col - 1]
                else:
                    mem[row][col] = max(mem[row - 1][col], mem[row][col - 1])
        minLen =  min(sLen, tLen)
        return (minLen == mem[row][col])

s = "AXY"
t = "ADXCPY"
result = Solution()
print(result.isSubsequence(s , t))