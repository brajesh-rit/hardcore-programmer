"""
https://practice.geeksforgeeks.org/problems/coin-change2448/1
Given a value N, find the number of ways to make change for N cents, if we have infinite supply of each of S = { S1, S2, .. , SM } valued coins.


Example 1:

Input:
n = 4 , m = 3
S[] = {1,2,3}
Output: 4
Explanation: Four Possible ways are:
{1,1,1,1},{1,1,2},{2,2},{1,3}.
"""
class Solution:
    def count(self, S, m, n):
        if n == 0 :
            return  1   # if array is empty then number of ways sum found is 1
        if m== 0:
            return 0

        if S[m-1] > n:
            return self.count(S,m-1, n)
        else:
            return self.count(S, m-1, n) + self.count(S,m , n -S[m-1])

n = 4  # sum target
m = 3
S = [1,2,3]
test = Solution()
print(test.count(S,m,n))