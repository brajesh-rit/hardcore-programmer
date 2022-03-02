"""
https://practice.geeksforgeeks.org/problems/search-in-a-matrix17201720/1
Given a matrix mat[][] of size N x M, where every row and column is sorted in increasing order,
and a number X is given. The task is to find whether element X is present in the matrix or not.


Example 1:

Input:
N = 3, M = 3
mat[][] = 3 30 38
         44 52 54
         57 60 69
X = 62
Output:
0
Explanation:
62 is not present in the
matrix, so output is 0

Example 2:

Input:
N = 1, M = 6
mat[][] = 18 21 27 38 55 67
X = 55
Output:
1
Explanation:
55 is present in the
matrix at 5th cell.

Your Task:
You don't need to read input or print anything. You just have to complete the function matSearch()
which takes a 2D matrix mat[][], its dimensions N and M and integer X as inputs and
returns 1 if the element X is present in the matrix and 0 otherwise.
"""

class Solution:
    def matSearch(self,mat, n, m, x):
        row = 0
        # set indexes for top right element
        col = m - 1
        while row < m and col >= 0:
            if mat[row][col] == x:
                print("n Found at ", row, ", ", col)
                return 1
            if mat[row][col] > x:
                col -= 1
            else:
                row += 1
        print("Element not found")
        return 0

# Driver Code
mat = [[10, 20, 30, 40],
       [15, 25, 35, 45],
       [27, 29, 37, 48],
       [32, 33, 39, 50]]
result = Solution()
result.matSearch(mat, 4, 4, 23)