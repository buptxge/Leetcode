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
    
        head1 = head
        for i in range(n-1):
            head1 = head1.next
            
        head2 = head
        head2_old = head2
        prev = None
        while head1.next is not None:
            head1 = head1.next
            prev = head2
            head2 = head2.next
            
        if prev is None:
            return head2_old.next
        else:
            prev.next = head2.next
            return head2_old