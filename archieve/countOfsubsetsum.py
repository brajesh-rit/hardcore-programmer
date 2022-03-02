class Solution:
    def perfectSum(self, arr, n, tot):
        #create the matix to store the value
        mem = [[-1 for x in range(tot + 1)] for x in range(n + 1)]
        #intial the base condition
        for row in range(n + 1):
            for col in range(tot + 1):
                if col == 0:
                    mem[row][col] = 1     #because empty set required that have count 1 for get sum 0(zero) hence all row first col is 1
                elif row == 0:
                    mem[row][col] = 0     #because array length is empty and try to get sum (something) that is not possible hence count is 0

        for row in range(1,n+1):
            for col in range(1,tot+1):
                if arr[row - 1] <= col:
                    mem[row][col] = mem[row -1][col - arr[row - 1]] + mem[row - 1][col]
                else:
                    mem[row][col] = mem[row - 1][col]
        return mem[n][tot]

arr = [2, 3, 5, 6, 8, 10]
tot = 11
n = 6
result = Solution()
print(result.perfectSum(arr,n,tot))