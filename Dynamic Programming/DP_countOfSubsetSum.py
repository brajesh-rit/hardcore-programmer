"""
https://practice.geeksforgeeks.org/problems/perfect-sum-problem5633/1
Given an array arr[] of integers and an integer sum, the task is to count all subsets of the given array with a sum equal to a given sum.

Note: Answer can be very large, so, output answer modulo 109+7
Example 1:
Input: N = 6, arr[] = {2, 3, 5, 6, 8, 10}
       sum = 10
Output: 3
Explanation: {2, 3, 5}, {2, 8}, {10}
"""
class Solution():
    def perfectSum1(self, arr, n, tot):
        def solve(arr, n, tot):
            if n== 0 and tot > 0:
                return 0
            if tot == 0:
                return 1
            if arr[n-1] > tot:
                return  solve(arr , n-1 ,tot)
            else:
                return solve(arr, n-1,tot) + solve(arr, n-1, tot- arr[n-1])

        return solve(arr, n, tot)

    def perfectSum(self, arr, n, tot):
        def solve(arr,n,tot):
            mem = [[-1 for x in range(tot + 1)]for x in range(n + 1)]
            for row in range(n+1):
                for col in range(tot + 1):
                    if col ==0 :             #phele col == 0 bhar dene se row/col =0 per 1 aa jata hai
                        mem[row][col] = 1
                    elif row == 0 :
                        mem[row][col] = 0
            for row in range(1,n+1):
                for col in range(1,tot + 1):
                    if arr[row -1] <= col:
                        mem[row][col] = mem[row - 1][col] + mem[row - 1][col - arr[row - 1]]
                    else:
                        mem[row][col] = mem[row - 1][col]
            return mem[n][tot]
        return solve(arr,n,tot)

test = Solution()
N = 6
arr = [2, 3, 5, 6, 8, 10]
sum = 10
print(test.perfectSum(arr,N,sum))