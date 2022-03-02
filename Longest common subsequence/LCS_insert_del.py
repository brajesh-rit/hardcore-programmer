class Solution:
    def minOperations(self, s1, s2):
        #https://practice.geeksforgeeks.org/problems/minimum-number-of-deletions-and-insertions0209/1
        #Given two strings str1 and str2. The task is to remove or insert the minimum number of characters
        # from/in str1 so as to transform it into str2. It could be possible that the same character needs to
        # be removed/deleted from one point of str1 and inserted to some another point.

        s1Len = len(s1)
        s2Len = len(s2)

        mem = [[-1 for x in range(s2Len + 1)] for x in range(s1Len + 1)]

        for row in range(s1Len + 1):
            for col in range(s2Len + 1):
                if row == 0 or col == 0:
                    mem[row][col] = 0

        for row in range(1,s1Len + 1):
            for col in range(1, s2Len + 1):
                if s1[row - 1] == s2[col - 1]:
                    mem[row][col] = 1 + mem[row - 1][col - 1]
                else:
                    mem[row][col] = max(mem[row - 1][col], mem[row][col - 1])

        lenLCS = mem[s1Len][s2Len]
        noDel = s1Len - lenLCS
        noIns = s2Len - lenLCS

        return  noDel + noIns

X = 'heap'
Y = 'pea'
result = Solution()
print(result.minOperations(X, Y ))