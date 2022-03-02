class Solution:
    def minimumNumberOfDeletions(self,S):
        #https://practice.geeksforgeeks.org/problems/minimum-deletitions1648/1
        #Given a string of S as input. Your task is to write a program to remove or delete the minimum number of characters from the string so that the resultant string is a palindrome.
        #Note: The order of characters in the string should be maintained.

        sLen = len(S)
        sRev =  S[::-1]
        mem = [[-1 for x in range(sLen + 1)] for x in range(sLen + 1)]
        for row in range(sLen + 1):
            for col in range(sLen + 1):
                if row == 0 or col ==0:
                    mem[row][col] = 0

        for row in range(1, sLen + 1):
            for col in range(1, sLen + 1):
                if S[row -1] == sRev[col - 1]:
                    mem[row][col] = mem[row - 1][col - 1] + 1
                else:
                    mem[row][col] =  max(mem[row - 1][col], mem[row][col - 1])

        return sLen -  mem[sLen][sLen]

s = "aebcbda"
result = Solution()
print(result.minimumNumberOfDeletions(s))