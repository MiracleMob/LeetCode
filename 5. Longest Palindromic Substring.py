class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # dp
        if not s:
            return ""
        st = 0
        ed = 0
        max_len = len_1 = len_2 = 0
        for i in range(len(s)):
            # 奇数
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                len_1 = right - left + 1
                left -= 1
                right += 1
            if len_1 > max_len:
                st = left + 1
                ed = right - 1
                max_len = len_1

            left = i
            right = i + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                len_2 = right - left + 1
                left -= 1
                right += 1
            if len_2 > max_len:
                st = left + 1
                ed = right - 1
                max_len = len_2
        return s[st:ed + 1]





