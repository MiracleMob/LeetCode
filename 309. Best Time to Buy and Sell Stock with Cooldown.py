class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        sell = [0] * len(prices)
        buy = [0] * len(prices)
        cool = [0] * len(prices)
        buy[0] = - prices[0]
        for i in range(1, len(prices)):
            buy[i] = max(buy[i - 1], cool[i - 1] - prices[i])
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
            cool[i] = max(cool[i - 1], buy[i - 1], sell[i - 1])

        return sell[-1]