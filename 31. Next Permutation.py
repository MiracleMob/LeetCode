class Solution(object):

    def reverse(self, nums):
        return list(reversed(nums))

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                k = nums[i - 1]
                index = i - 1
                break
        if index == -1:
            return nums.reverse()
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > k:
                nums[i], nums[index] = nums[index], nums[i]
                break
        nums[index + 1:] = self.reverse(nums[index + 1:])

        return nums