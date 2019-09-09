class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        window = []
        max_len = 0
        length = 0
        for c in s:
            while c in window:
                window.pop(0)
                length -= 1
            window.append(c)
            length += 1
            max_len = max(max_len, length)
        return max_len