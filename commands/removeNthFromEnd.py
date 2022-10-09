# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next == None:
            return None
        
        nodes = []
        temp = head
        while (temp != None):
            nodes.append(temp)
            temp = temp.next
        
        if n == 1:
            prev = nodes[-(n+1)]
            prev.next = None
        elif n == len(nodes):
            head = nodes[-(n-1)]
        else:
            prev = nodes[-(n+1)]
            next = nodes[-(n-1)]
            prev.next = next
        return head