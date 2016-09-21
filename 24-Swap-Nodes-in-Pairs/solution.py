# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = ListNode(0)
        result = pre
        pre.next = head
        
        while pre.next and pre.next.next:
            a = pre.next
            b = pre.next.next
            pre.next, a.next, b.next = b, b.next, a
            pre = a
        return result.next
            