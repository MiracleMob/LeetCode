class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # dp sum(p) = (t+sum(s))/ 2
        if (sum(nums) + S) % 2 == 1 or sum(nums) < S:
            return 0
        P = (sum(nums) + S) // 2
        dp = [1] + [0] * P
        for num in nums:
            for i in range(P, num - 1, -1):
                dp[i] += dp[i - num]

        return dp[-1]

