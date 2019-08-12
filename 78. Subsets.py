class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # dp[i] = dp[i-1] + [each+[nums[i]] for i in dp[i-1]]
        dp = [[]]
        for i in range(len(nums)):
            dp = dp + [each+[nums[i]] for each in dp]
        return dp