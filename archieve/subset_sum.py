class Solution(object):
    def isSubsetSum(self,set, n, sum):
        if sum > 0 and n == 0:
            return False
        if sum == 0:
            return  True

        if set[n -1] > sum:
            return  self.isSubsetSum(set, n-1,sum)

        if self.isSubsetSum(set, n-1, sum) or self.isSubsetSum(set, n-1, sum - set[n-1]):
            return  True
        else:
            return False

    mem = {}
    def isSubsetSum1(self,set, n, sum):
        com_key = str(sum) + ',' + str(n)
        if com_key in self.mem:
            return self.mem[com_key]
        if sum > 0 and n == 0:
            return False
        if sum == 0:
            return  True
        if set[n -1] > sum:
            self.mem[com_key] = self.isSubsetSum1(set, n-1,sum)
            return  self.mem[com_key]

        if self.isSubsetSum1(set, n-1, sum) or self.isSubsetSum1(set, n-1, sum - set[n-1]):
            self.mem[com_key] = True
            return  True
        else:
            self.mem[com_key] = False
            return False

    def isSubsetSum2(self, set, n, sum):

        # intialized with -1 of all the two dimension array
        mem = [[-1 for x in range(sum + 1)] for x in range(n + 1)]   # work as column then row

        #intialized the base condition
        for row in range(n+1):   #  outer is row inner is column
            for col in range(sum + 1):
                if col == 0:                  # order of if statement is important because of mem[0][0] place whatever is comming that should be first if condition
                    mem[row][col] = True
                elif row == 0:
                    mem[row][col] = False

        # for row in range(1,n+1):
        #     for col in range(1,sum + 1):
        #         if set[row -1] > col:
        #             mem[row][col] = mem[row - 1][col]
        #         if mem[row - 1][col] or mem[row -1][col - set[row -1]]:
        #             mem[row][col] = True
        #         else:
        #             mem[row][col] = False

        #@@@@@@@@@@@@@@@@@@@@@@ Above logic is not working because I didnot work partical and writing way. always write the logic in paper and then write in code
        # @@very important @@@@  in for loop all are in row and column only never put in parameter value

        for row in range(1, n + 1):
            for col in range(1, sum + 1):
                if set[row -1] <= col:   # current value is array is less then sum means I can take that value or not
                    mem[row][col] = mem[row - 1][col - set[row -1]] or mem[row - 1][col]   # first condition is taking the value hence decrease from sum *** second condition is not taking hence not decrease
                else:
                    mem[row][col] = mem[row - 1][col]  # if sum is greater than current array value it means it is not consider at all

        return mem[n][sum]

result = Solution()
set = [2, 3, 7, 8, 10]
sum = 11
n = 5
# set = [3, 34, 4, 12, 5, 2]
# sum = 30
# n = 6
print( result.isSubsetSum2(set, n , sum))