# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """   
        return self.compare(p, q)
    
    def compare(self, first, second):
        if first == None and second == None:
            return True
        elif first == None or second == None:
            return False
        elif first.val != second.val:
            return False
        else:
            return self.compare(first.left, second.left) and self.compare(first.right, second.right)
        