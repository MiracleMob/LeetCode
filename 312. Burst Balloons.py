class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        dp = [[0] * len(nums) for _ in range(len(nums))]
        for l in range(2, len(nums)):
            for i in range(0, len(nums) - l):
                j = i + l
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j],
                                   dp[i][k] + dp[k][j] + nums[i] * nums[k] *
                                   nums[j])

        return dp[0][len(nums) - 1]


