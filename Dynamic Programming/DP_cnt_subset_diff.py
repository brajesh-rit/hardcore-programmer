class Solution:
    def diff_subsetSum(self, arr, diff):
        arr_len = len(arr)
        tot = sum(arr)
        tot = int((diff + sum(arr)) / 2)
        mem = [[-1 for x in range(tot + 1)] for x in range(arr_len + 1)]

        for row in range(arr_len + 1):
            for col in range(tot + 1):
                if col == 0:
                    mem[row][col] = 1
                elif row == 0:
                    mem[row][col] =  0

        for row in range(1, arr_len + 1):
            for col in range(1, tot + 1):
                if arr[row -1] <= col:
                    mem[row][col] = mem[row -1][col - arr[row - 1]] + mem[row - 1][col]
                else:
                    mem[row][col] = mem[row - 1][col]
        return mem[arr_len][tot]            # always take last of array value not + 1 becuase it start from 0

arr = [1,1,2,3]
diff = 1

result = Solution()
print( result.diff_subsetSum(arr, diff))