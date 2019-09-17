class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        tmp = 1
        for i in range(len(s)-1, -1, -1):
            ans += tmp * (ord(s[i]) - ord('A') + 1)
            tmp *= 26
        return ans