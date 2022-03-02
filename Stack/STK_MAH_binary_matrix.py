"""
https://leetcode.com/problems/maximal-rectangle/
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
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

    def maximalRectangle(self, matrix):
        rows = len(matrix)
        if rows == 0:
            return 0
        cols = len(matrix[0])
        arr = [int(matrix[0][j]) for j in range(cols)]
        max_area = self.getMaxArea(arr)
        for row in range(1, rows):
            for col in range(cols):
                if matrix[row][col] == '0':
                    arr[col] = 0
                else:
                    arr[col] = arr[col] + int(matrix[row][col])
            max_area = max(max_area,self.getMaxArea(arr))
        return max_area


#matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
matrix = []
print(Solution().maximalRectangle(matrix))