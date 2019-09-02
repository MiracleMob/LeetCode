class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        st = ed = -1
        for i in range(len(nums)):
            if nums[i] == target:
                if st == -1:
                    st = i
                if i > ed:
                    ed = i
                ans = [st, ed]
        return [st,ed]


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        st = self.index(nums, target, True)
        if st == len(nums) or nums[st] != target:
            return [-1, -1]
        ed = self.index(nums, target, False) - 1
        return [st, ed]

    def index(self, nums, target, left):
        st = 0
        ed = len(nums)
        while st < ed:
            mid = (st + ed) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                ed = mid
            else:
                st = mid + 1
        return st

