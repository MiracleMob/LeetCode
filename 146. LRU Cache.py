class ListNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = ListNode(None, None)
        self.tail = ListNode(None, None)
        self.capacity = capacity
        self.hash_map = {}

        self.head.next = self.tail
        self.tail.pre = self.head

    def move_to_end(self, key):
        node = self.hash_map[key]
        node.pre.next = node.next
        node.next.pre = node.pre

        node.next = self.tail
        node.pre = self.tail.pre

        self.tail.pre.next = node
        self.tail.pre = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.hash_map:
            return -1
        self.move_to_end(key)

        return self.hash_map[key].value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.hash_map:
            self.hash_map[key].value = value
            self.move_to_end(key)
        else:
            if len(self.hash_map) == self.capacity:
                self.hash_map.pop(self.head.next.key)
                self.head.next = self.head.next.next
                self.head.next.pre = self.head

            Node = ListNode(key, value)
            Node.next = self.tail
            Node.pre = self.tail.pre
            self.tail.pre.next = Node
            self.tail.pre = Node
            self.hash_map[key] = Node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)