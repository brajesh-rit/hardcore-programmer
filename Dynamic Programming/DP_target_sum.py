"""
https://leetcode.com/problems/target-sum/
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
"""

class Solution(object):
    def findTargetSumWays(self, nums, target):
        leng = len(nums)
        tot = sum(nums)
        if target > tot:
            return 0
        tot = int((target + tot) / 2)
        mem = [[-1 for x in range(tot + 1)] for x in range(leng + 1)]

        for row in range(leng + 1):
            for col in range(tot + 1):
                if col == 0:
                    mem[row][col] = 1
                elif row == 0:
                    mem[row][col] = 0

        for row in range(1, leng + 1):
            for col in range(1, tot + 1):
                if nums[row - 1] <= col:
                    mem[row][col] = mem[row - 1][col - nums[row - 1]] + mem[row - 1][col]
                else:
                    mem[row][col] = mem[row - 1][col]
        return mem[leng][tot]


    def findTargetSumWays_memo(self, nums, target):
        mem = {}
    
        def dfs(index, s):
            if index == len(nums):
                return s == target

            if (index, s) in mem:
                return mem[(index, s)]

            mem[(index, s)] = dfs(index+1, s+nums[index]) + \
                              dfs(index+1, s-nums[index])

            return mem[(index, s)]

        return dfs(0, 0)
nums = [1,1,1,1,1]
target = 3

# nums = [1]
# target = 2
# #
result = Solution()
print(result.findTargetSumWays(nums, target))