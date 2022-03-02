#https://leetcode.com/problems/binary-tree-maximum-path-sum/
#A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence
#  has an edge connecting them. A node can only appear in the sequence at most once.
# Note that the path does not need to pass through the root.
#The path sum of a path is the sum of the node's values in the path.
#Given the root of a binary tree, return the maximum path sum of any path.
class node:
    def __init__(self,x):
        self.val = 0 if x is None else x
        self.left = None
        self.right = None
class Solution:

    def createTree(self,arr):
        leng = len(arr)
        if leng == 0:
            return None
        mid =  leng// 2
        tree = node(arr[mid])
        tree.left = self.createTree(arr[0:mid])
        tree.right = self.createTree(arr[mid+1:leng])
        return tree

    def printTree(self,tree,level):
        if tree is None:
            return
        self.printTree(tree.left,level+ 1)
        print(' '*level*4,'->',tree.val)
        self.printTree(tree.right,level+ 1)
        return
    res = float('-inf')
    def sumPathTree(self,tree):
        def dfs(tree):
            if tree is None:
                return 0
            lsum = dfs(tree.left)
            rsum = dfs(tree.right)
            temp = max(max(lsum, rsum) + tree.val, tree.val)
            ans = max(temp ,lsum + rsum + tree.val)
            self.res = max(self.res, ans)
            return temp
        dfs(tree)
        return self.res
res = Solution()
#arr = [1,2,3,4,5,6,7,8,9]
arr = [1,-2,3]
tree = res.createTree(arr)
res.printTree(tree, 0)
print(res.sumPathTree(tree))
