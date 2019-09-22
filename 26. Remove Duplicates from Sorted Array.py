class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        while i < len(nums):
            while i < len(nums) - 1 and nums[i + 1] == nums[i]:
                i += 1
            nums[j] = nums[i]
            i += 1
            j += 1
        return j
