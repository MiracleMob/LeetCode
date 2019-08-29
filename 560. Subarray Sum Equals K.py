class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # hash_dict = {sum:sum_num}
        hash_dict = dict()
        hash_dict[0] = 1
        ans = 0
        Sum = 0
        for i in range(len(nums)):
            Sum += nums[i]
            if Sum - k in hash_dict:
                ans += hash_dict[Sum - k]
            if Sum not in hash_dict:
                hash_dict[Sum] = 1
            else:
                hash_dict[Sum] += 1

        return ans

