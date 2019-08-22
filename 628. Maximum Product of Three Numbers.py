class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return None
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]
        max_1 = -1001
        max_2 = -1001
        max_3 = -1001
        min_1 = 1001
        min_2 = 1001

        for num in nums:
            if num > max_1:
                max_1, max_2, max_3 = num, max_1, max_2
            elif num > max_2:
                max_2, max_3 = num, max_2
            elif num > max_3:
                max_3 = num
            if num < min_1:
                min_1, min_2 = num, min_1
            elif num < min_2:
                min_2 = num

        return max(max_1 * max_2 * max_3, max_1 * min_1 * min_2)
