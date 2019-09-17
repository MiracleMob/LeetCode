class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        n = len(heights)
        left = [0] * n
        right = [0] * n
        left[0] = -1
        right[-1] = n
        for i in range(1, n):
            tmp = i - 1
            while tmp >= 0 and heights[tmp] >= heights[i]:
                tmp = left[tmp]
            left[i] = tmp
        for j in range(n - 2, -1, -1):
            tmp = j + 1
            while tmp < n and heights[tmp] >= heights[j]:
                tmp = right[tmp]
            right[j] = tmp
        ans = 0
        for i in range(n):
            ans = max(ans, (right[i] - left[i] - 1) * heights[i])

        return ans


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights = [0] + heights + [0]
        stack = []
        ans = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                ans = max(ans, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return ans
