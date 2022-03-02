#Given an array of integers, find the closest (not considering distance, but value)
# smaller on left of every element. If an element has no smaller on the left side, print -1.

class Solution:
    def nextSmallerElement(self, arr,n):
        s = []
        ans = []
        for i in range(n):
            if len(s) == 0:    # we can take if not s since blank object also known as false
                ans.append(-1)
            else:
                while len(s) > 0 and s[len(s) - 1] >= arr[i]: #stack end of array is top remember it
                    s.pop()
                if len(s) == 0:
                    ans.append(-1)
                else:
                    ans.append(s[len(s) - 1])
            s.append(arr[i])
        return ans
arr = [4,5,2,10,8]
n = len(arr)
print(Solution().nextSmallerElement(arr,n))