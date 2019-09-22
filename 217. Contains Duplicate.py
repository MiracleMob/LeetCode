class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m = dict()

        for num in nums:
            if num not in m:
                m[num] = 1
            else:
                return True
        return False