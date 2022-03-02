#https://leetcode.com/problems/binary-tree-maximum-path-sum/submissions/
#A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the
# sequence has an edge connecting them. A node can only appear in the sequence at most once.
# Note that the path does not need to pass through the root.
# working code in leetcode


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
            temp = max(max(l,r) + root.val, root.val)
            ans =  max(temp, l+r+ root.val)
            self.res =  max(self.res, ans)
            return temp
        dfs(root)
        # we are essentially calculating is the number of nodes,
        # so in order to return the edge count, we simply reduce the answer by 1
        return self.res

result = Solution()
output = result.sorted_array_to_bst([1,2,3])
#result.printTree(output)

print(result.maxPathSum(output))