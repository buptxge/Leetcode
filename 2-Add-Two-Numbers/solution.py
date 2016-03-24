# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if (l1 == None) and (l2 == None):
            return None
            
        result = ListNode(0)
        head = result
        carry = 0
        while True:
            has_next = False
            if l1 != None:
                result.val += l1.val
                l1 = l1.next
            if l2 != None:
                result.val += l2.val
                l2 = l2.next
                
            carry = result.val / 10
            result.val = result.val % 10
            if (l1) or (l2) or (carry == 1):
                result.next = ListNode(carry)
                result = result.next

        return head
                
                