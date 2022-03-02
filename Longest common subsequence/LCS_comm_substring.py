class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        #https://practice.geeksforgeeks.org/problems/longest-common-substring1452/1
        #Given two strings. The task is to find the length of the longest common substring.
        mem = [[-1 for x in range(n+1)] for x in range(m+1)]

        # intialize with base condition
        for row in range(m + 1):
            for col in range(n+1):
                if row == 0 or col == 0:
                    mem[row][col] = 0

        for row in range(1, m +1):
            for col in range(1,n + 1):
                if S2[row - 1] == S1[col - 1]:            #Take care about S1 string is matching with n and S2 string is matching with m  so row is with S1 string
                    mem[row][col] = mem[row -1][col-1] + 1
                else:
                    mem[row][col] = 0                       # string count is not increased and initalize with 0 because match not found
        # Take transverse all over the matix which is max value just take that value and return
        # Becuase substring is present in any place of the string.
        result = 0
        for row in range(m):
            val = max(mem[row])
            result =  max(result, val)
        return result

x = 6
y = 6
s1 = 'ABCDGH'
s2 = 'ACDGHR'
result = Solution()
print(result.longestCommonSubstr( s1, s2, x, y))