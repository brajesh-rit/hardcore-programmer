"""
https://practice.geeksforgeeks.org/problems/longest-common-substring1452/1
Given two strings. The task is to find the length of the longest common substring.


Example 1:

Input: S1 = "ABCDGH", S2 = "ACDGHR"
Output: 4
Explanation: The longest common substring
is "CDGH" which has length 4.
"""
class Solution:
    def longestCommonSubstr1(self, s1, s2, n, m):
        def solve(s1, s2, n, m, cnt):
            if m == 0 or n == 0:
                return 0
            if s1[n-1] == s2[m-1]:
                cnt = solve(s1,s2,n-1,m-1, cnt +1 )
            cnt = max(cnt, max(solve(s1,s2,n-1,m,0), solve(s1,s2,n,m-1,0)))

            return cnt
        result = solve(s1, s2, n, m , 0)
        return result

    def longestCommonSubstr3(self,s1, s2, n, m):
        # Create DP table
        mem = [[0 for col in range(m + 1)] for row in range(2)]
        res = 0

        for row in range(1, n + 1):
            for col in range(1, m + 1):
                if (s1[row - 1] == s2[col - 1]):
                    mem[row % 2][col] = mem[(row - 1) % 2][col - 1] + 1
                    res = max(mem[row % 2][col], res)
                else:
                    mem[row % 2][col] = 0
        return res

    def longestCommonSubstr2(self, s1, s2, n, m):
        mem = [[-1 for _ in range(m+1)]for _ in range(n+1)]

        for row in range(n+1):
            for col in range(m+1):
                if row == 0 or col == 0 :
                    mem[row][col] = 0

        for row in range(1,n+1):
            for col in range(1,m+1):
                if s1[row-1] == s2[col-1]:
                    mem[row][col] = mem[row-1][col-1] + 1
                else:
                    mem[row][col] = 0
        res = 0                          # don't take - inf because count never go less than 0
        for i in range(m+1):
            res = max(res,mem[n][i])
        return res


S1 = "ABCDGH"
S2 = "ACDGHR"
n = 6
m = 6
test = Solution()
print(test.longestCommonSubstr(S1,S2,n,m))