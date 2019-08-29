# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        hash_set = set()
        node = head
        while node:
            if node in hash_set:
                return node
            hash_set.add(node)
            node = node.next

        return None


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        meet = self.find(head)
        if not meet:
            return None
        p1 = head
        p2 = meet
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1

    def find(self, head):
        # 找到相遇点
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return fast

        if not fast or not fast.next:
            return None

