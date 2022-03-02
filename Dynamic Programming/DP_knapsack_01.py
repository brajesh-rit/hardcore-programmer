"""
https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1
You are given weights and values of N items, put these items in a knapsack of capacity W to get 
the maximum total value in the knapsack. Note that we have only one quantity of each item.
In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which represent 
values and weights associated with N items respectively. Also given an integer W which 
represents knapsack capacity, find out the maximum value subset of val[] such that sum of 
the weights of this subset is smaller than or equal to W. You cannot break an item, either pick 
the complete item or don’t pick it (0-1 property).

Example 1:
Input:
N = 3
W = 4
values[] = {1,2,3}
weight[] = {4,5,1}
Output: 3
"""
class Solution(object):
    def knapSack(self, W, wt, val, n):
        # Base case
        if n == 0 or W == 0:
            return 0

        # If weight of the nth item is
        # more than Knapsack of capacity W,
        # then this item cannot be included
        # in the optimal solution
        if (wt[n - 1] > W):
            return self.knapSack(W, wt, val, n - 1)

        # return the maximum of two cases:
        # (1) nth item included
        # (2) not included
        else:
            return max(
                val[n - 1] + self.knapSack( W - wt[n - 1], wt, val, n - 1),
                self.knapSack(W, wt, val, n - 1))

    # memorized array of the value
    def knapSack1(self, W, wt, val, n):

        #intialized with -1 of all the two dimension array
        mem = [[-1 for x in range(W + 1)] for x in range(n + 1)]

        #base condition
        if n == 0 or W == 0:
            return 0

        #if value is store in memorisation matix then simple return
        if mem[n][W] != -1:
            return mem[n][W]

        #choice diagram code
        if wt[n-1] > W:
            mem[n][W] = self.knapSack1(W, wt, val, n - 1)  #if you don't want the include current item
            return mem[n][W]
        elif wt[n-1] <= W:
            mem[n][W] = max( val[n - 1] + self.knapSack1( W - wt[n - 1], wt, val, n - 1),  # if you want to include or not depend upon where value is comming max
                            self.knapSack1(W, wt, val, n - 1))
            return mem[n][W]

    def knapSack(self, W,wt,val,n):
        # intialized with -1 of all the two dimension array
        mem = [[-1 for i in range(W+1)]for i in range(n+1)]

        # intialized the base condition
        for row in range(n+1):
            for col in range(W+1):
                if row == 0 or col ==0:
                    mem[row][col] = 0
        
        # choice diagram code
        for row in range(1,n+1):
            for col in range(1, W+1):
                if wt[row-1] > col:
                    mem[row][col] = mem[row -1][col]
                elif wt[row - 1] <= col:
                    mem[row][col] = max(val[row - 1] + mem[row-1][col-wt[row-1]], mem[row-1][col])
        return mem[n][W]


result = Solution()
# val = [1, 4, 5, 7]
# wt = [1,3,4,5]
# W = 7
# n = len(val)

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print( result.knapSack2(W, wt, val, n))