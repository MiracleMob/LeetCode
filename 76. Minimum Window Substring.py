from collections import Counter


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_c = Counter(t)
        s_c = Counter()
        left = 0
        right = 0
        min_len = float("inf")
        res = ""
        while right < len(s):
            s_c[s[right]] += 1
            right += 1
            while all(map(lambda x: s_c[x] >= t_c[x], t_c.keys())):
                if right - left < min_len:
                    res = s[left:right]
                    min_len = right - left
                s_c[s[left]] -= 1
                left += 1
        return res



