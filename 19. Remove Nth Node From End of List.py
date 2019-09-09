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
        ans = head
        l1 = l2 = head
        l3 = ListNode(0)
        l3.next = head
        for _ in range(n):
            l2 = l2.next
        while l2:
            l2 = l2.next
            l1 = l1.next
            l3 = l3.next
        if l1 == head:
            return ans.next
        else:
            l3.next = l1.next
            l1.next = None
        return ans

