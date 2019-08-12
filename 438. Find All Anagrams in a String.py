class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        target = {}
        window = {}
        ans = []
        # 记录target字符串中字符个数
        for c in p:
            target[c] = target.get(c, 0) + 1
        # 双指针
        left = 0
        right = 0
        while right < len(s):
            if s[right] not in p:
                window.clear()
                left = right + 1
                right += 1
            else:
                window[s[right]] = window.get(s[right], 0) + 1
                if right - left + 1 == len(p):
                    if window == target:
                        ans.append(left)
                    window[s[left]] -= 1
                    left += 1
                right += 1

        return ans



