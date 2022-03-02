"""
https://practice.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1/
Given an array of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.

Example 1:
Input:
N = 6
arr[] = {3, 34, 4, 12, 5, 2}
sum = 9
Output: 1
Explanation: Here there exists a subset with
sum = 9, 4+3+2 = 9.
"""

class Solution:
    def isSubsetSum1(self, n, arr, sum):
        def solve( n, arr, sum):
            if n == 0 and sum > 0:
                return False
            elif sum == 0:
                return True
            if arr[n-1] > sum:
                return solve(n-1,arr,sum)
            else:
                return solve(n-1,arr,sum) or solve(n-1,arr,sum - arr[n-1])
        if solve(n, arr, sum):
            return 1
        else:
            return 0

    mem = {}
    def isSubsetSum2(self,n,arr,sum):
        def solve( n, arr, sum):
            key = str(n) + ',' + str(sum)
            if key in self.mem:
                return self.mem[key]
            if n == 0 and sum > 0:
                self.mem[key] = False
                return False
            elif sum == 0:
                self.mem[key] = True
                return True
            if arr[n-1] > sum:
                self.mem[key] = solve(n-1,arr,sum)
                return self.mem[key]
            else:
                self.mem[key] = solve(n-1,arr,sum) or solve(n-1,arr,sum - arr[n-1])
                return self.mem[key]
        if solve(n, arr, sum):
            return 1
        else:
            return 0

    def isSubsetSum(self, n, arr, sum):
        mem = [[-1 for x in range(sum+1)] for x in range(n + 1)]

        for row in range(n+1):
            for col in range(sum+1):
                if col == 0:
                    mem[row][col] = True
                if row == 0 and col > 0:
                    mem[row][col] = False

        for row in range(1,n+1):
            for col in range(1,sum+1):
                if arr[row -1] > col:
                    mem[row][col] = mem[row-1][col]
                else:
                    mem[row][col] = mem[row-1][col] or mem[row-1][col-arr[row-1]]
        if mem[n][sum]:
            return 1
        else:
            return 0

result = Solution()
arr = [3, 34, 4, 12, 5, 2]
n = len(arr)
sum = 50
#arr = [43, 87, 98, 86, 69, 95, 98, 90, 67, 27, 96, 86, 36, 65, 100, 8, 79, 24, 3, 28, 15, 99, 27, 12, 5, 42, 1, 9, 66, 95, 72, 9, 34, 21, 94, 54, 67, 43, 43, 86, 69, 90, 71, 4, 6, 70, 11, 85, 93, 66, 64, 60, 64, 90, 23, 20, 84, 23, 29, 1, 70, 52, 9, 3, 73, 54, 56, 91, 96, 50, 76, 17, 91, 46, 72, 96, 68, 35, 80, 60, 100, 43, 71, 15, 85, 94, 34, 20, 16, 14, 20, 85, 18, 81, 39, 42, 86, 46, 32, 34]
#n = len(arr)
#sum = 4877
print(result.isSubsetSum(n,arr,sum))