# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        
        temp = head
        while (l1 != None or l2 != None) :
            if (l1 == None) :
                temp.next = l2
                temp = temp.next
                l2 = l2.next
            elif (l2 == None):
                temp.next = l1
                temp = temp.next
                l1 = l1.next
            elif (l1.val <= l2.val):
                temp.next = l1
                temp = temp.next
                l1 = l1.next
            else:
                temp.next = l2
                temp = temp.next
                l2 = l2.next
            
        return head