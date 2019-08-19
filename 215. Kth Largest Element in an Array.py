class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 快速选择
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = self.partation(nums, low, high)
            if mid == k - 1:
                return nums[k - 1]
            elif mid > k - 1:
                high -= 1
            else:
                low += 1
        return None

    def partation(self, nums, low, high):
        left = low + 1
        right = high
        # nums[low], nums[(low+high)//2] = nums[(low+high)//2], nums[low]
        bound = nums[low]
        # 快速排序, 选择num[bound]正确的位置
        while left <= right:
            while left < right and nums[left] >= bound:
                left += 1
            while nums[right] < bound:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
            else:
                break
        # 将bound放到正确的位置
        nums[low], nums[right] = nums[right], nums[low]
        return right