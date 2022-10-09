# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nodes = []
        if head == None:
            return False
        
        while head.next != None:
            if head not in nodes:
                nodes.append(head)
            else:
                return True
            head = head.next
        return False