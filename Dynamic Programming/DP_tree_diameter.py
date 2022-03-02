#https://practice.geeksforgeeks.org/problems/diameter-of-binary-tree/1
#The diameter of a tree (sometimes called the width) is the number of nodes on 
#the longest path between two end nodes. The diagram below shows two trees each 
#with diameter nine, the leaves that form the ends of the longest path are shaded 
#(note that there is more than one path in each tree of length nine, but no path longer 
#than nine nodes). 

#https://leetcode.com/problems/diameter-of-binary-tree/
# leetcode decrease 1 in final answer I don't know why?
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
    def diameterOfBinaryTree(self, root):
        def dfs(root):
            if root is None:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            temp = max(l,r) + 1
            print(root.val)
            ans =  max(temp, l+r+1)
            self.res =  max(self.res, ans)
            return temp
        dfs(root)
        return self.res

result = Solution()
output = result.sorted_array_to_bst([1,2,3,4,5])
#result.printTree(output)

print(result.diameterOfBinaryTree(output))