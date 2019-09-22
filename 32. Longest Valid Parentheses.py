class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        stack = []
        ans = []

        for i in range(len(s)):
            if stack and s[i] == ')':
                ans.append(stack.pop())
                ans.append(i)
            if s[i] == '(':
                stack.append(i)
        ans.sort()

        i = 0
        n = len(ans)
        res = 0
        while i < n:
            j = i
            while j < n - 1 and ans[j + 1] - ans[j] == 1:
                j += 1
            res = max(res, j - i + 1)
            i = j + 1
        return res


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dp = [0] * (len(s))
        ans = 0
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                elif s[i - 1] == ')' and i - dp[i - 1] - 1 >= 0 and s[
                    i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                if dp[i] > ans:
                    ans = dp[i]
        return ans

