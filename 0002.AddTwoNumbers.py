# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def setValue(self, value):
        self.val = value
    def setNext(self, nextValue):
        self.next = nextValue
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        suma = True
        l3 = None
        node = None
        countNodes = 0
        lleva = 0
        while suma == True:
            newValue = l1.val+l2.val+lleva
            if newValue > 9:
                lleva = 1
                if l3 == None:
                    l3 = ListNode(val=(newValue-10))
                    countNodes += 1
                else:
                    node = l3
                    for i in range(countNodes-1):
                        node = node.next
                    node.next = ListNode(val=(newValue-10))
                    countNodes += 1
            else:
                lleva = 0
                if l3 == None:
                    l3 = ListNode(val=newValue)
                    countNodes += 1
                else:
                    node = l3
                    for i in range(countNodes-1):
                        node = node.next
                    node.next = ListNode(val=newValue)
                    countNodes += 1
            if (l1.next == None) and (l2.next == None):
                if lleva == 1:
                    l1 = ListNode()
                    l2 = ListNode()
                else:
                    suma = False
                    break
            elif l1.next == None:
                l1 = ListNode()
                l2 = l2.next
            elif l2.next == None:
                l2 = ListNode()
                l1 = l1.next
            else:
                l1 = l1.next
                l2 = l2.next
        return l3