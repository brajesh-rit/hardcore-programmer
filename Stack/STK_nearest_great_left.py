#Given an array of integers, find the closest (not considering distance, but value) greater on left of every element.
# If an element has no greater on the left side, print -1.

class Solution:
    def nextLargerElement(self, arr,n):
        s = []
        ans = []
        for i in range(n):  # check in reverse count down last is -1 otherwise it will not count 0
            if len(s) == 0:    # we can take if not s since blank object also known as false
                ans.append(-1)
            else:
                while len(s) > 0 and s[len(s) - 1] <= arr[i]: #stack end of array is top remember it
                    s.pop()
                if len(s) == 0:
                    ans.append(-1)
                else:
                    ans.append(s[len(s) - 1])
            s.append(arr[i])
        return ans


arr = [1, 3, 2, 4]
n = len(arr)
print(Solution().nextLargerElement(arr,n))