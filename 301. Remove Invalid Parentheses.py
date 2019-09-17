class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def isvalid(s):
            cnt = 0
            for c in s:
                if c == '(':
                    cnt += 1
                if c == ')':
                    cnt -= 1
                if cnt < 0:
                    return False
            return cnt == 0

        def dfs(s, st, l, r):
            if l == 0 and r == 0:
                if isvalid(s):
                    self.ans.append(s)
                return
            for i in range(st, len(s)):
                if i - 1 >= st and s[i] == s[i - 1]:
                    continue
                if r > 0 and s[i] == ')':
                    dfs(s[:i] + s[i + 1:], i, l, r - 1)
                if l > 0 and s[i] == '(':
                    dfs(s[:i] + s[i + 1:], i, l - 1, r)

        self.ans = []
        l = r = 0
        for c in s:
            if c == '(':
                l += 1
            if c == ')':
                if l == 0:
                    r += 1
                else:
                    l -= 1

        dfs(s, 0, l, r)
        return self.ans

