class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # dp dp[i][j] = word1前i个 和 word2前j个最短编辑距离

        m = len(word1)
        n = len(word2)
        if n * m == 0:
            return max(n, m)

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(n + 1):
            dp[0][i] = i
        for i in range(m + 1):
            dp[i][0] = i
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1],
                                       dp[i - 1][j - 1] - 1)
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1],
                                       dp[i - 1][j - 1])
        return dp[m][n]