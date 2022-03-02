class Solution:
    def equalPartition(self, N, arr):
        tot = sum(arr)                  # sum function is independent is not part of list
        if tot % 2 != 0:
            return False
        tot =  int(tot / 2)       #'float' object cannot be interpreted as an integer

        mem = [[-1 for x in range(tot + 1)] for x in range (N + 1) ]

        for row in range(N + 1):
            for col in range(tot + 1):
                if col == 0:
                    mem[row][col] =True
                elif row == 0:
                    mem[row][col] = False

        for row in range(1, N+1):
            for col in range(1,tot+1):
                if arr[row -1] <= col:
                    mem[row][col] = mem[row -1][col - arr[row-1]] or mem[row -1][col]
                else:
                    mem[row][col] = mem[row -1][col]

        return mem[N][tot]

arr = [1,3,5]
tot = 11
n = 3

result = Solution()
print( result.equalPartition( n , arr))