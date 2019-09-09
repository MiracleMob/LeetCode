class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        pre_max = nums[0]
        pre_min = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            cur_max = max(pre_max * nums[i], pre_min * nums[i], nums[i])
            cur_min = min(pre_max * nums[i], pre_min * nums[i], nums[i])
            ans = max(ans, cur_max)
            pre_max = cur_max
            pre_min = cur_min
        return ans