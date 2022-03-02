
class node:
    def __init__(self ):
        self.val = 0
        self.left = None
        self.right = None
class Solution:
    def tree_sorted(self,arr):
        leng = len(arr)
        if leng == 0:
            return None
        tree = node()
        mid = len(arr)//2
        tree.val = arr[mid]
        tree.left = self.tree_sorted(arr[0:mid])
        tree.right = self.tree_sorted(arr[mid + 1:leng])
        return tree

    def printTree(self,Tree, level = 1):
        if Tree is None:
            return
        self.printTree(Tree.left, level+ 1)
        print(' '* 4 * level,'->',Tree.val)
        self.printTree(Tree.right, level + 1)
        return
    res = 0
    def treeDiameter(self,tree):
        if tree is None:
            return 0
        lLen = self.treeDiameter(tree.left)
        rLen = self.treeDiameter(tree.right)
        temp = max(lLen , rLen) + 1
        ans = lLen+ rLen + 1
        self.res = max(self.res,ans)  # collect maximum value of every node in global variable
        return temp

    def main(self,tree):
        self.treeDiameter(tree)
        return self.res

arr = [1,2,3,4,5,6,7,8,9]
res = Solution()

Tree = res.tree_sorted(arr)
#res.printTree(Tree)
print(res.main(Tree))