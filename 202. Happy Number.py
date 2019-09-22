class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        res = n
        while 1:
            nums = str(res)
            res = 0
            for num in nums:
                res += int(num) ** 2
            if res == 1:
                return True
            if res in s:
                return False
            else:
                s.add(res)


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = n
        fast = sum(int(num) ** 2 for num in str(n))

        while slow != fast:
            slow = sum(int(num) ** 2 for num in str(slow))
            fast = sum(int(num) ** 2 for num in str(fast))
            fast = sum(int(num) ** 2 for num in str(fast))
        return slow == 1