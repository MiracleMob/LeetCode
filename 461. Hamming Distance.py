class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ans = 0
        while x > 0 or y > 0:
            if y % 2 != x % 2:
                ans += 1
            y = y // 2
            x = x // 2

        return ans

