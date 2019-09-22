class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # dp[i][j] = s[:i+1] 和 p[:j+1] 是否匹配

        s_len = len(s)
        p_len = len(p)

        dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]
        dp[0][0] = True
        for i in range(p_len):
            # 没有匹配的情况
            if p[i] == '*' and dp[0][i - 1]:
                dp[0][i + 1] = True
        for i in range(s_len):
            for j in range(p_len):
                if s[i] == p[j] or p[j] == '.':
                    dp[i + 1][j + 1] = dp[i][j]
                elif p[j] == '*':
                    if p[j - 1] != s[i]:
                        dp[i + 1][j + 1] = dp[i + 1][j - 1]
                    if p[j - 1] == s[i] or p[j - 1] == '.':
                        # 多个匹配 没有匹配 一个匹配
                        dp[i + 1][j + 1] = (dp[i][j + 1] or dp[i + 1][j - 1] or
                                            dp[i + 1][j])
        return dp[-1][-1]
