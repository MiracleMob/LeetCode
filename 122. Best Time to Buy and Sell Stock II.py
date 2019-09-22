class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 峰谷法
        n = len(prices)
        ans = 0
        i = 0
        while i < n - 1:
            # valley
            while i < n - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]

            while i < n - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]

            ans += peak - valley

        return ans


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 只计算上坡路
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                ans += prices[i] - prices[i - 1]

        return ans