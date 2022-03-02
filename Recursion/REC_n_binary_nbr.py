"""
https://practice.geeksforgeeks.org/problems/print-n-bit-binary-numbers-having-more-1s-than-0s0252/1
Print N-bit binary numbers having more 1s than 0s
Given a positive integer N, the task is to find all the N bit binary numbers having more than or equal 1’s than 0’s for
any prefix of the number.

Example 1:
Input:  N = 2
Output: 11 10
Explanation: 11 and 10 have more than
or equal 1's than 0's
Example 2:

Input:  N = 3
Output: 111 110 101
Explanation: 111, 110 and 101 have more
than or equal 1's than 0's

"""

class Solution:
    result = []
    def solve (self, nOne, nZero, nTot,out):
        if nTot == 0:
            self.result.append(out)
            return
        if nZero < nOne:
            op1 = out + '0'
            self.solve(nOne,nZero+1,nTot-1, op1)
        op2 = out + '1'
        self.solve(nOne+1,nZero,nTot-1, op2)
        return

    def NBitBinary(self, N):
        out = '1'
        nOne = 1
        nZero = 0
        N = N - 1
        self.solve(nOne,nZero,N,out)
        return self.result

N = 5
result = Solution()
print(result.NBitBinary(N))