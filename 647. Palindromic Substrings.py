class Solution:
    def countSubstrings(self, s: str) -> int:
        # 中心
        ans = 0
        for i in range(len(s)):
            ans += self.count(s, i, i)
            ans += self.count(s, i, i + 1)

        return ans

    def count(self, s, st, ed):
        count = 0
        while st >= 0 and ed < len(s) and s[st] == s[ed]:
            st -= 1
            ed += 1
            count += 1

        return count
