#https://www.geeksforgeeks.org/boolean-parenthesization-problem-dp-37/
#https://practice.geeksforgeeks.org/problems/boolean-parenthesization5610/1
#Count the number of ways we can parenthesize the expression so that the value of expression evaluates to true.
#Let the input be in form of two arrays one contains the symbols (T and F) in order and the other contains operators (&, | and ^}
class Solution:
    def countWays(self,len,arr):
        return  self.solve(arr, 0 , len-1,True)

    def solve_recursive(self, arr, i , j, isTrue):
        if i > j:
            return False
        if i == j:
            if isTrue == True:
                return True if arr[i] == 'T' else False    #New style of else if attention : is not there
            else:
                return True if arr[i] == 'F' else False   #else part means False chahiya aur arr me bhi char F return True else FALSE
        ans = 0
        # k should move for i+1 to j-1 end is j since final is excluded in range
        # T|F&T^F
        for k in range(i + 1, j,2):
            LeftTrue = self.solve(arr,i, k-1, True)
            LeftFalse = self.solve(arr,i, k-1, False)
            RightTrue = self.solve(arr,k+1, j,True)
            RightFalse = self.solve(arr, k + 1, j, False)

            if arr[k] == '&':
                if isTrue == True:
                    ans =  ans + (LeftTrue * RightTrue)
                else:
                    ans = ans +  (LeftFalse * RightTrue
                                  + LeftTrue * RightFalse
                                  + LeftFalse * RightFalse)
            elif arr[k] == '|':
                if isTrue == True:
                    ans = ans + (LeftTrue * RightTrue
                                 + LeftTrue * RightFalse
                                 + LeftFalse * RightTrue)
                else:
                    ans = ans + (LeftFalse * RightFalse)
            elif arr[k] == '^':
                if isTrue == True:
                    ans = ans + (LeftTrue * RightFalse
                                 + LeftFalse * RightTrue)
                else:
                    ans =  ans + (LeftTrue * RightTrue
                                  + LeftFalse * RightFalse)
        return  ans

    # Below code for memorization
    mem = {}
    def solve(self, arr, i , j, isTrue):
        key = str(i) + ',' + str(j) + ('T' if isTrue else 'F')
        if key in self.mem:
            return self.mem[key]
        if i > j:
            self.mem[key] = False
            return False
        if i == j:
            if isTrue == True:
                self.mem[key] = True if arr[i] == 'T' else False    #New style of else if attention : is not there
                return self.mem[key]
            else:
                self.mem[key] = True if arr[i] == 'F' else False   #else part means False chahiya aur arr me bhi char F return True else FALSE
                return self.mem[key]
        ans = 0
        # k should move for i+1 to j-1 end is j since final is excluded in range
        # T|F&T^F
        for k in range(i + 1, j,2):
            LeftTrue = self.solve(arr,i, k-1, True)
            LeftFalse = self.solve(arr,i, k-1, False)
            RightTrue = self.solve(arr,k+1, j,True)
            RightFalse = self.solve(arr, k + 1, j, False)

            if arr[k] == '&':
                if isTrue == True:
                    ans =  ans + (LeftTrue * RightTrue)
                else:
                    ans = ans +  (LeftFalse * RightTrue
                                  + LeftTrue * RightFalse
                                  + LeftFalse * RightFalse)
            elif arr[k] == '|':
                if isTrue == True:
                    ans = ans + (LeftTrue * RightTrue
                                 + LeftTrue * RightFalse
                                 + LeftFalse * RightTrue)
                else:
                    ans = ans + (LeftFalse * RightFalse)
            elif arr[k] == '^':
                if isTrue == True:
                    ans = ans + (LeftTrue * RightFalse
                                 + LeftFalse * RightTrue)
                else:
                    ans =  ans + (LeftTrue * RightTrue
                                  + LeftFalse * RightFalse)
        self.mem[key] = ans
        return  ans




arr = 'T|F^F&T|F^F^F^T|T&T^T|F^T^F&F^T|T^F'
n = len(arr)
result = Solution()
#print(result.solve(arr, 0 , n-1, True))
print(result.countWays(n,arr))