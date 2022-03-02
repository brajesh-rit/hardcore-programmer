"""
https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1
0 - 1 Knapsack Problem
You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
Note that we have only one quantity of each item.
In other words, given two integer arrays val[0..N-1] and wt[0..N-1] which represent values and weights associated with N
items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of
val[] such that sum of the weights of this subset is smaller than or equal to W.
You cannot break an item, either pick the complete item or don’t pick it (0-1 property).

Example 1:

Input:
N = 3
W = 4
values[] = {1,2,3}
weight[] = {4,5,1}
Output: 3
Succeful run in
"""
class Solution:
    def knapSack1(self, W, wt, val, n):
        if n ==0:
            return 0
        if wt[n-1] > W:
            return self.knapSack1(W,wt,val, n-1)
        else:
            return max(val[n-1] + self.knapSack1(W-wt[n-1],wt,val,n-1),
                                  self.knapSack1(W,wt,val,n-1))

    mem = {}
    def knapSack2(self, W, wt, val, n):
        key = str(W) + ','+str(n)
        if key in self.mem:
            return self.mem[key]
        if n ==0:
            return 0
        if wt[n-1] > W:
            self.mem[key] = self.knapSack2(W,wt,val, n-1)
            return self.mem[key]
        else:
            self.mem[key] = max(val[n-1] + self.knapSack2(W-wt[n-1],wt,val,n-1),
                                  self.knapSack2(W,wt,val,n-1))
            return self.mem[key]

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
                else:
                    mem[row][col] = max(val[row - 1] + mem[row-1][col-wt[row-1]], mem[row-1][col])
        return mem[n][W]


N = 3
W = 4
values = [1, 2, 3]
weight = [4, 5, 1]
res = Solution()
print(res.knapSack(W,weight,values,N))