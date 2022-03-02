#https://practice.geeksforgeeks.org/problems/longest-repeating-subsequence2004/1
#Given a string str, find the length of the longest repeating subsequence such that it can be found
# twice in the given string. The two identified subsequences A and B can use the same ith character
# from string str if and only if that ith character has different indices in A and B.

class Solution:
    def LongestRepeatingSubsequence(self, str):
        sLen = len(str)
        mem =  [[-1 for x in range(sLen + 1)] for x in range(sLen + 1)]

        for row in range(sLen + 1):
            for col in range(sLen + 1):
                if row == 0  or col == 0:
                    mem[row][col] = 0

        for row in range(1, sLen + 1):
            for col in range(1,sLen + 1):
                if str[row - 1] == str[col - 1] and row != col:
                    mem[row][col] = 1 + mem[row - 1][col - 1]
                else:
                    mem[row][col] = max(mem[row -1][col], mem[row][col - 1])

        return mem[sLen][sLen]

str = "AABEBCDD"
result = Solution()
print(result.LongestRepeatingSubsequence(str))
