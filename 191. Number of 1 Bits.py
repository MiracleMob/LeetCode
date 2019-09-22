class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        mask = 1
        while n!= 0:
            if n & mask == 1:
                ans += 1
            n = n >> 1
        return ans