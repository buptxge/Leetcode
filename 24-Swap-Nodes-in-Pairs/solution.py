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
        cur = head
        pre = ListNode()
        pre.next = cur
        
        while cur and cur.next:
            pre.next = cur.next
            cur.next = cur.next.next
            pre.next.next = cur
            pre = cur
            cur = cur.next
            
        return head
            