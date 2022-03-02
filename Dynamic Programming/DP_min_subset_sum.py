"""
https://practice.geeksforgeeks.org/problems/minimum-sum-partition3317/1
Given an integer array arr of size N, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum and find the minimum difference

Example 1:

Input: N = 4, arr[] = {1, 6, 11, 5}
Output: 1
Explanation:
Subset1 = {1, 5, 6}, sum of Subset1 = 12
Subset2 = {11}, sum of Subset2 = 11
"""

class Solution:
    def minDifference(self, arr, n):
        tot = sum(arr)
        mem = [[-1 for x in range(tot+1)] for x in range(n+1)]

        for row in range(n+1):
            for col in range(tot + 1):
                if col == 0:
                    mem[row][col] = True
                elif row == 0:
                    mem[row][col] = False

        for row in range(1,n+1):
            for col in range(1,tot + 1):
                if arr[row - 1] > col:
                    mem[row][col] = mem[row -1][col]
                else:
                    mem[row][col] = mem[row -1][col] or mem[row -1][col - arr[row - 1]]
        # store the only true value of the last row of matrix in to contender array which will give the answer
        pTot = []
        for i in range(int((tot+ 1)/2)):
            if mem[n][i]:
                pTot.append(i)

        # intialize with +ve infinte of the value  focus on float there is not int function
        ans = float('inf')
        for i in pTot:
            ans = min(ans, (tot - 2 * i ))

        return ans

test = Solution()
arr =[5, 6, 6, 5, 7, 4, 7, 6]
n = 4
print(test.minDifference(arr,n))