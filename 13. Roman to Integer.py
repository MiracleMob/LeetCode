class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        map_dict = {'I': (1, 1), 'V': (5, 2), 'X': (10, 3), 'L': (50, 4),
                    'C': (100, 5), 'D': (500, 6), 'M': (1000, 7)}

        ans = map_dict[s[-1]][0]
        n = len(s)
        for i in range(n - 2, -1, -1):
            if map_dict[s[i]][1] >= map_dict[s[i + 1]][1]:
                ans += map_dict[s[i]][0]
            else:
                ans -= map_dict[s[i]][0]

        return ans