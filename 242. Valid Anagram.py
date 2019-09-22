class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        c_map = {}
        for c in s:
            if c not in c_map:
                c_map[c] = 1
            else:
                c_map[c] += 1

        for c in t:
            if c not in c_map:
                return False
            else:
                c_map[c] -= 1
                if c_map[c] < 0:
                    return False

        return True