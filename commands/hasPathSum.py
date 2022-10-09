# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root == None:
            return False
        return self.findSum(root, 0, targetSum)
    def findSum(self, root, thisSum, targetSum):
        thisSum += root.val
        if root.left == None and root.right == None:
            if thisSum == targetSum:
                return True
            else:
                return False
        elif root.left == None:
            return self.findSum(root.right, thisSum, targetSum)
        elif root.right == None:
            return self.findSum(root.left, thisSum, targetSum)
        else:
            return self.findSum(root.left, thisSum, targetSum) or self.findSum(root.right, thisSum, targetSum)