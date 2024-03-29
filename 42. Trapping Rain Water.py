class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        max_left[0] = height[0]
        max_right[-1] = height[-1]
        for i in range(1, len(height)):
            max_left[i] = max(height[i], max_left[i - 1])
        for i in range(n - 2, -1, -1):
            max_right[i] = max(height[i], max_right[i + 1])

        ans = 0

        for i in range(n):
            ans += (min(max_left[i], max_right[i]) - height[i])
        return ans