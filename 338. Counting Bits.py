class Solution(object):

    # 1.奇数：dp[i] = dp[i-1]
    # 2.偶数: dp[i] = dp[i/2]
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0] * (num + 1)
        for i in range(0, num + 1):
            if i % 2 == 0:
                dp[i] = dp[i / 2]
            else:
                dp[i] = dp[i - 1] + 1

        return dp
