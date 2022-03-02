#https://leetcode.com/problems/longest-palindromic-substring/
#Given a string s, return the longest palindromic substring in s

class Solution(object):
    def longestPalindrome(self, s):
        sLen =  len(s)
        sRev =  s[::-1]

        mem = [[-1 for x in range(sLen + 1)] for x in range(sLen + 1)]

        for row in range(sLen + 1):
            for col in range(sLen + 1):
                if row == 0 or col == 0:
                    mem[row][col]= 0

        for row in range(1, sLen + 1):
            for col in range(1, sLen + 1):
                if s[row - 1] == sRev[col - 1]:
                    mem[row][col] = 1 + mem[row - 1][col - 1]
                else:
                    mem[row][col] = max(mem[row -1][col], mem[row][col - 1])
        return mem[sLen][sLen]

s = "babad"
result = Solution()
print(result.longestPalindrome(s))