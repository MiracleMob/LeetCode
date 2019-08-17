class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set()
        for num in nums:
            if num in num_set:
                return num
            num_set.add(num)
