class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sm = (1 + n) * n / 2
        for num in nums:
            sm -= num

        return sm