class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 == 1:
            return False
        target = sum_nums // 2
        dp = [False for _ in range(target + 1)]
        length = len(nums)
        for i in range(target + 1):
            if nums[0] == i:
                dp[i] = True
                break

        for i in range(1, length):
            for j in range(target, -1, -1):
                if nums[i] <= j:
                    dp[j] = dp[j] or dp[j - nums[i]]
                else:
                    break

        return dp[-1]