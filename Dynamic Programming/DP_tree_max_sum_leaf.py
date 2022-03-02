#https://practice.geeksforgeeks.org/problems/maximum-path-sum/1
#Given a binary tree in which each node element contains a number.
# Find the maximum possible path sum from one leaf node to another leaf node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sorted_array_to_bst(self, nums):
        if not nums:
            return None
        mid_val = len(nums) // 2
        node = TreeNode(nums[mid_val])
        node.left = self.sorted_array_to_bst(nums[:mid_val])
        node.right = self.sorted_array_to_bst(nums[mid_val + 1:])
        return node

    def printTree(self,node, level=0):
        if node != None:
            self.printTree(node.left, level + 1)
            print(' ' * 4 * level + '->', node.val)
            self.printTree(node.right, level + 1)

    res = float('-inf')
    def maxPathSum(self, root):
        def dfs(root):
            if root is None:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            temp = max(l,r) + root.val
            ans =  max(temp, l+r+ root.val)
            self.res =  max(self.res, ans)
            return temp
        dfs(root)
        # we are essentially calculating is the number of nodes,
        # so in order to return the edge count, we simply reduce the answer by 1
        return self.res

result = Solution()
output = result.sorted_array_to_bst([-9,6,-10])
result.printTree(output)

print(result.maxPathSum(output))

