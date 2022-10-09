# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        elements = []
        curr = head
        prev = None
        while curr != None:
            if curr.val in elements:
                prev.next = curr.next
                
            else:
                elements.append(curr.val)
                prev = curr
            curr = curr.next
        return head
        