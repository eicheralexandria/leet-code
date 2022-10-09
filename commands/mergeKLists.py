# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        list1 = self.merge2Lists(lists[0], lists[1])
        self.displayList(list1)
        
        finalList = self.merge2Lists(list1, lists[2])
        
        self.displayList(finalList)
        return finalList
        
    def merge2Lists(self, list1, list2):
        finalList = None
        finalPointer = None
        curr1 = list1
        curr2 = list2
        
        while (curr1 != None and curr2 != None):
            print("1. curr1.val", curr1.val)
            print("2. curr2.val", curr2.val)
            
            if curr1.val == curr2.val:
                print(curr1.val, "==", curr2.val)
                temp1 = curr1.next
                temp2 = curr2.next
                if finalList == None:
                    finalList = curr1
                else:
                    finalPointer.next = curr1
                curr1.next = curr2
                finalPointer = curr2
                finalPointer.next = None
                
            elif curr1.val < curr2.val:
                print(curr1.val, "<", curr2.val)
                temp1 = curr1.next
                temp2 = curr2.next
                if finalList == None:
                    finalList = curr1
                else:
                    finalPointer.next = curr1
                curr1.next = curr2
                finalPointer = curr2
                finalPointer.next = None
            else:
                print(curr1.val, ">", curr2.val)
                temp1 = curr1.next
                temp2 = curr2.next
                if finalList == None:
                    finalList = curr2
                else:
                    finalPointer.next = curr2
                curr2.next = curr1
                finalPointer = curr1
                finalPointer.next = None
                
            if temp1 == None and temp2 == None:
                break
            elif temp1 == None:
                finalPointer = curr2
                curr2 = temp2
            elif temp2 == None:
                finalPointer = curr1
                curr1 = temp1
            else:
                curr1 = temp1
                curr2 = temp2
                
            print("3. curr1.val", curr1.val)
            print("4. curr2.val", curr2.val)
            print("finalPointer:", finalPointer.val)
            self.displayList(finalList)
            print("")

        return finalList
                
                
    def displayList(self, l):
        while l != None:
            print(l.val)
            l = l.next

            
        
sol = Solution()
node1 = ListNode(1, ListNode(4, ListNode(5, None)))
node2 = ListNode(1, ListNode(3, ListNode(4, None)))
node3 = ListNode(2, ListNode(6, None))
lists = [node1, node2, node3]
sol.mergeKLists(lists)







