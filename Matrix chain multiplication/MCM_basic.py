#https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/
#https://practice.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1
#Given a sequence of matrices, find the most efficient way to multiply these matrices together.
# The efficient way is the one that involves the least number of multiplications.

class Solution:
    def MatrixChainOrder1(self, arr, i, j):
        if i >= j:
            return  0
        minVal = float('inf')
        for k in range(i, j):
            temp = self.MatrixChainOrder(arr,i,k) + self.MatrixChainOrder(arr , k + 1, j) + (arr[i -1] * arr[k] * arr[j] )
            minVal = min(minVal, temp)
        return minVal

    def matrixMultiplication(self, N, arr):
        return self.MatrixChainOrder(arr, 1, N - 1)

    mem = {}
    def MatrixChainOrder(self, arr, i, j):
        key = str(i) + ',' + str(j)
        if key in self.mem:
            return self.mem[key]
        if i >= j:
            return  0
        minVal = float('inf')
        for k in range(i, j):
            temp = self.MatrixChainOrder(arr,i,k) + self.MatrixChainOrder(arr , k + 1, j) + (arr[i -1] * arr[k] * arr[j] )
            minVal = min(minVal, temp)
            self.mem[key] = minVal
        return minVal

    def MatrixChainOrder2(self, n, p):
        # For simplicity of the program,
        # one extra row and one
        # extra column are allocated in m[][].
        # 0th row and 0th
        # column of m[][] are not used
        mem = [[-1 for x in range(n)] for x in range(n)]

        # intialize only digonal of the matrix because cost is zero when multiplying one matrix.
        for row in range(1, n):
            mem[row][row] = 0

        # L is chain length.
        for d in range(1, n):
            for row in range(1, n - d):
                col = row + d
                mem[row][col] = float('inf')
                for k in range(row, col):
                    cost = mem[row][k] + mem[k + 1][col] + p[row - 1] * p[k] * p[col]
                    mem[row][col] = min(cost, mem[row][col])

        return mem[1][n - 1]


#arr = [40,20,30,10,30]
#n = len(arr)
#arr = [3,3,3]
#n = len(arr)
arr = [2,2,4,3]
n = len(arr)
result = Solution()
print(result.MatrixChainOrder2(n, arr))
#print(result.MatrixChainOrder2(arr, 1 , n -1))