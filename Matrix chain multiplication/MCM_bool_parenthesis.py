"""
https://www.geeksforgeeks.org/boolean-parenthesization-problem-dp-37/
Given a boolean expression with following symbols.

Symbols
    'T' ---> true
    'F' ---> false
And following operators filled between symbols.
"""
class Solution:
    mem = {}
    def solve(self, arr, i, j, isTrue) :
        key = str(i) + ','+str(j)+ ','+ ('T' if isTrue else 'F')
        if key in self.mem:
            return self.mem[key]
        if i > j:
            self.mem[key] = False
            return False
        if i == j:
            if isTrue:
                self.mem[key] = True if arr[i] == 'T' else False
                return self.mem[key]
            else:
                self.mem[key] = True if arr[i] == 'F' else False
                return self.mem[key]
        ans = 0
        for k in range(i+1,j,2):
            lt = self.solve(arr,i,k-1,True)
            lf = self.solve(arr,i,k-1, False)
            rt = self.solve(arr,k+1,j,True)
            rf = self.solve(arr,k+1,j,False)
            if arr[k] == '|':
                if isTrue:
                   ans = ans + (lt * rf + lf * rt + lt * rt)
                else:
                    ans = ans + (lf * rf)
            elif arr[k] == '&':
                if isTrue:
                    ans += (lt * rt)
                else:
                    ans += (lf * rt + lt * rf + lf * rf)
            elif arr[k] == '^':
                if isTrue:
                    ans += (lt * rf + lf * rt)
                else:
                    ans += (lt * rt + lf * rf)
        self.mem[key] = ans
        return ans

arr = 'T|F^F&T|F^F^F^T|T&T^T|F^T^F&F^T|T^F'
#arr = 'T^F&T'
n = len(arr)
result = Solution()
print(result.solve(arr, 0 , n-1, True))
#print(result.countWays(n,arr))