class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n] * m
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                if i == 0 and j > 0:
                    dp[i][j] = dp[i][j - 1]
                if i > 0 and j == 1:
                    dp[i][j] = dp[i - 1][j]
                if i > 0 and j > 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]


