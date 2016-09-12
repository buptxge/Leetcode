class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        listall = []
        for listnode in lists:
            while listnode:
                listall.append(listnode.val)
                listnode = listnode.next
        listall.sort()
        res = p = ListNode(0)
        for i in listall:
            p.next = p = ListNode(i)
        return res.next