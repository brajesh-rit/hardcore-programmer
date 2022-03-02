"""
https://practice.geeksforgeeks.org/problems/longest-common-subsequence-1587115620/1
Longest Common Subsequence
Given two sequences, find the length of longest subsequence present in both of them. Both the strings are of uppercase.

Example 1:

Input:
A = 6, B = 6
str1 = ABCDGH
str2 = AEDFHR
Output: 3
Explanation: LCS for input Sequences
“ABCDGH” and “AEDFHR” is “ADH” of
length 3.
"""

class Solution:
    def lcs1(self, x, y, s1, s2):
        if x == 0 or y == 0:
            return 0
        if s1[x-1] == s2[y-1]:
            return self.lcs1(x-1, y-1, s1, s2) + 1
        else:
            return max(self.lcs1(x-1,y , s1,s2), self.lcs1(x,y-1,s1,s2))

    def lcs(self, x, y, s1, s2):
        mem = [[-1 for _ in range(y+1)] for _ in range(x+1)]

        for row in range(x+1):
            for col in range(y+1):
                if row == 0 or col == 0:
                    mem[row][col] = 0

        for row in range(1,x+1):
            for col in range(1, y+1):
                if s1[row-1] == s2[col-1]:
                    mem[row][col] = mem[row-1][col-1] + 1
                else:
                    mem[row][col] = max(mem[row-1][col],mem[row][col-1])

        return mem[x][y]


# A = 6
# B = 6
# str1 = "ABCDGH"
# str2 = "AEDFHR"

A = 4
B = 3
str1 = "ABCD"
str2 = "ABC"
test = Solution()
print(test.lcs(A,B,str1,str2))