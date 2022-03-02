class Solution:
    ans = []
    def flatten(self, arr):
        for cs in arr:
            if isinstance(cs,list):
                self.flatten(cs)
            else:
                self.ans.append(cs)

arr = [1, 6, [2, 3,[1, 2, [1, 2]]], 4,[989898,2,3,[9,0,0,[9,0]]], [5, [6, [7, [1,2, [1, 2]]]]]]

result = Solution()
result.flatten(arr)
print(result.ans)