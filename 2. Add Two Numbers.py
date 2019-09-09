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
        carry = 0
        ans = tmp = ListNode(0)
        while l1 and l2:
            tmp.next = ListNode(0)
            tmp = tmp.next
            tmp.val = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            l1 = l1.next
            l2 = l2.next

        while l1:
            t = l1.val
            l1.val = (t + carry) % 10
            carry = (t + carry) // 10
            tmp.next = l1
            l1 = l1.next
            tmp = tmp.next
        while l2:
            t = l2.val
            l2.val = (t + carry) % 10
            carry = (t + carry) // 10
            tmp.next = l2
            l2 = l2.next
            tmp = tmp.next
        if carry > 0:
            tmp.next = ListNode(carry)

        return ans.next


