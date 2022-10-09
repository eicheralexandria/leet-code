"""
* program name: Add two numbers
* description: Add two numbers each represented by a singly linked list. 
*   type: ListNode
*   name: l1
* input:
*   type: ListNode
*   name: l2
* end
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def run(self, args):
        list_one = self.convertToLinkedList(args["l1"])
        list_two = self.convertToLinkedList(args["l2"])
        ans = self.addTwoNumbers(list_one, list_two)
        return self.convertToInt(ans)

    def convertToLinkedList(self, num):
        num_str = str(num)
        head = ListNode(int(num_str[0]))
        temp = head
        for element in num_str[1:]:
            temp.next = ListNode(int(element))
            temp = temp.next
        return head

    def convertToInt(self, l):
        ans = ""
        while (l != None):
            ans += str(l.val)
            l = l.next
        return ans

    def addTwoNumbers(self, l1, l2):
        returnNode = ListNode()
        currentNode = returnNode
        
        value = l1.val + l2.val
        carry = 0
        if value > 9:
            value = value - 10
            carry = 1
            
        currentNode.val = value
        if l1.next or l2.next:
            nextNode = ListNode()
            currentNode.next = nextNode
            currentNode = currentNode.next
        else:
            if carry == 1:
                nextNode = ListNode(1)
                currentNode.next = nextNode
                
        while l1.next or l2.next:
            l1 = l1.next
            l2 = l2.next
            
            if l1 == None:
                l1 = ListNode(0)
            if l2 == None:
                l2 = ListNode(0)
            value = l1.val + l2.val + carry
            carry = 0
            if value > 9:
                value = value - 10
                carry = 1
                
            currentNode.val = value
            if l1.next or l2.next:
                nextNode = ListNode()
                currentNode.next = nextNode
                currentNode = currentNode.next
                
            else:
                if carry == 1:
                    nextNode = ListNode(1)
                    currentNode.next = nextNode

        return returnNode




