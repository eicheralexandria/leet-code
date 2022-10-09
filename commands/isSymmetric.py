# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        first = root.left
        second = root.right
        
        return self.compare(first, second)
    
    def compare(self, first, second):
        if first == None and second == None:
            return True
        elif first == None or second == None:
            return False
        elif first.val != second.val:
            return False
        else:
            return self.compare(first.left, second.right) and self.compare(first.right, second.left)
        