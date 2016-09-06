# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next is None:
            return None
    
        head1 = head
        for i in range(n-1):
            head1 = haed1.next
            
        head2 = head
        prev = None
        while head1.next is not None:
            head1 = head1.next
            prev = head2
            head2 = head2.next
            
        prev.next = head2.next
        return head2