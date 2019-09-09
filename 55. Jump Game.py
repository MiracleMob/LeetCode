class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        st = 0
        ed = 0
        while st <= ed and ed < len(nums):
            ed = max(ed, st + nums[st])
            st += 1
        return ed >= (len(nums) - 1)

