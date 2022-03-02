class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #Below function just create tree for sorted array
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

    def heightTree(self,root):
        if root is None:
            return 0
        l = self.heightTree(root.left)
        r = self.heightTree(root.right)
        return (1+ max(l,r))

result = Solution()
output = result.sorted_array_to_bst([1,2,3,4,5,6,7,8,9,10])
result.printTree(output)

print(result.heightTree(output))