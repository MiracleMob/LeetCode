# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 递归，归并排序
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        # find mid
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(mid)

        # merge
        t = ans = ListNode(0)
        while left and right:
            if left.val < right.val:
                t.next = left
                left = left.next
            else:
                t.next = right
                right = right.next
            t = t.next

        if left:
            t.next = left
        else:
            t.next = right

        return ans.next

