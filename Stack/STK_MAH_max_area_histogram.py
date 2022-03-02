"""
https://practice.geeksforgeeks.org/problems/maximum-rectangular-area-in-a-histogram-1587115620/1
Find the largest rectangular area possible in a given histogram where the largest rectangle can
be made of a number of contiguous bars. For simplicity,
assume that all bars have the same width and the width is 1 unit,
there will be N bars height of each bar will be given by the array arr.

Example 1:

Input:
N = 7
arr[] = {6,2,5,4,5,1,6}
Output: 12
Explanation:
"""

class Solution:
    def smallNearesLeft(self, arr,n):
        s = []
        ans = []
        for i in range(n):
            if len(s) == 0:
                ans.append(-1)
            else:
                while len(s) > 0 and s[len(s) - 1][0] >= arr[i]:
                    s.pop()
                if len(s) == 0:
                    ans.append(-1)
                else:
                    ans.append(s[len(s) - 1][1])
            s.append((arr[i], i))
        return ans


    def smallNearesRight(self, arr, n):
        s = []
        ans = []
        for i in range(n-1,-1,-1):
            if len(s) == 0:
                ans.append(n)
            else:
                while len(s) > 0 and s[len(s) - 1][0] >= arr[i]:
                    s.pop()
                if len(s) == 0:
                    ans.append(n)
                else:
                    ans.append(s[len(s) - 1][1])
            s.append((arr[i], i))
        ans = ans[::-1]
        return ans

    # Function to find largest rectangular area possible in a given histogram.
    def getMaxArea(self, histogram):
        n = len(histogram)
        nsl = self.smallNearesLeft(histogram,n)
        nsr = self.smallNearesRight(histogram,n)
        width = [nsr[i] - nsl[i] - 1 for i in range(n)]
        area = [histogram[i] * width[i] for i in range(n)]
        return max(area)

arr = [6,2,5,4,5,1,6]
n = len(arr)
print(Solution().getMaxArea(arr))