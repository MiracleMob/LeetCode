class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p1 = p2 = 0

        while p1 < len(nums):
            if nums[p1] != 0:
                nums[p2] = nums[p1]
                p2 += 1
            p1 += 1

        for i in range(p2, len(nums)):
            nums[i] = 0


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p1 = p2 = 0

        while p1 < len(nums):
            if nums[p1] != 0:
                nums[p2], nums[p1] = nums[p1], nums[p2]
                p2 += 1
            p1 += 1

