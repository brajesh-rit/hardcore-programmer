"""
https://practice.geeksforgeeks.org/problems/rod-cutting0840/1
Given a rod of length N inches and an array of prices, price[] that contains prices of all pieces of size smaller than N. Determine the maximum value obtainable by cutting up the rod and selling the pieces.

Example 1:

Input:
N = 8
Price[] = {1, 5, 8, 9, 10, 17, 17, 20}
Output:
22
Explanation:
The maximum obtainable value is 22 by
cutting in two pieces of lengths 2 and
6, i.e., 5+17=22.
"""
class Solution:
    # max_val = float('-inf')
    # def cutRod1(self, price, n):
    #     def solve(price, n):
    #         if n <= 0:
    #             return 0
    #         for i in range(n):
    #             for j in range(i):
    #                 self.max_val =  max(self.max_val, price[j] + solve(price, i - j-1 ) )
    #             return self.max_val
    #     return solve(price, n )

    def cutRod2(self,price,n):
        val = [-1 for _ in range(n+1)]
        val[0] = 0
        for i in range(1, n+1):
            max_val = float('-inf')
            for j in range(i):
                max_val = max(max_val, price[j] + val[i -j-1])
            val[i] = max_val
        return val[n]

    def cutRod(self, price, n):
        # if property of rod is not given then create yourself here it to property (length and price)
        rodLen = list(range(1,n+1))               # list in-line function convert the range of number to list
        mem = [[-1 for x in range(n+1)] for x in range(n+1)]

        #base condition
        for row in range(n + 1):
            for col in range(n+1):
                if col == 0:
                    mem[row][col] = 0
                elif row == 0:
                    mem[row][col] = 0

        for row in range(1,n+1):
            for col in range(1,n+1):
                if rodLen[row - 1] <= col:
                    mem[row][col] = max(price[row-1] + mem[row ][col - rodLen[row - 1] ], mem[row - 1][col])    # unbounded  variation here mem[row][col - rodLen[row - 1]] instead of mem[row -1][col - rodLen[row - 1]]
                else:
                    mem[row][col] = mem[row - 1][col]

        return mem[n][n]
test = Solution()
# arr = [1, 5, 8, 9, 10, 17, 17, 20]
# n = 8
arr = [1, 5, 8, 9]
n = 4
print(test.cutRod2(arr, n))