class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_set = set(nums)
        max_cnt = 0
        for num in hash_set:
            if num - 1 not in hash_set:
                current = num
                cnt = 1
                while current + 1 in hash_set:
                    current += 1
                    cnt += 1
                max_cnt = max(max_cnt, cnt)

        return max_cnt

