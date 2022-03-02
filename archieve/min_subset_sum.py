class Solution:
    def minDifference(self, arr, n):
        tot = sum(arr)
        mem = [[-1 for x in range(tot + 1)] for x in range(n + 1)]
        # initialize base condition
        for row in range(n + 1):
            for col in range(tot + 1):
                if col == 0:         # get sum zero with any number of array element that always be true
                    mem[row][col] = True
                elif row == 0:      #get all sum without taking help of any of element that always be false
                    mem[row][col] = False

        #figure out the possible sum of given array subset.
        for row in range(1, n+1):
            for col in range(1, tot + 1):
                if arr[row - 1] <= col:
                    mem[row][col] = mem[row - 1][col - arr[row - 1]] or mem[row - 1][col]
                else:
                    mem[row][col] = mem[row - 1][col]
        #store the only true value of the last row of matrix in to contender array which will give the answer
        con = []
        for col in range(int((tot+ 1)/2)):
            if mem[n][col]:
                con.append(col)

        result = float('inf')     # intialize with +ve infinte of the value  focus on float there is not int function
        for i in con:
            result = min(result , (tot - 2*i))

        return result

# arr = [1, 6, 11, 5]
# n = 4
arr = [5, 6, 6, 5, 7, 4, 7, 6]
n = 8

result = Solution()
print(result.minDifference(arr,n))