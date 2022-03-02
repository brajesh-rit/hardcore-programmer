#https://practice.geeksforgeeks.org/problems/form-a-palindrome1455/1
#Given a string, find the minimum number of characters to be inserted to convert it to palindrome.
class Solution:
    def countMin(self, str):
        sLen = len(str)
        sRev = str[::-1]

        mem =  [[-1 for x in range(sLen + 1)] for x in range(sLen + 1)]
        for row in range(sLen + 1):
            for col in range(sLen + 1):
                if row == 0 or col == 0:
                    mem[row][col] = 0

        for row in range(1, sLen + 1):
            for col in range(1, sLen + 1):
                if str[row -1] == sRev[col - 1]:
                    mem[row][col] = 1 + mem[row - 1][col - 1]
                else:
                    mem[row][col] = max (mem[row - 1][col], mem[row][col - 1])

        return sLen - mem[sLen][sLen]   # total lenght - len(lcs) = # min insertion /# min deletion both are same

s = "abcd"
result = Solution()
print(result.countMin(s))