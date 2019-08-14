class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #结合律
        ans = 0
        for num in nums:
            ans ^= num
        return ans