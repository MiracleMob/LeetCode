# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    ans = float('-inf')

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def max_gain(node):
            if not node:
                return 0
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            price_path = node.val + left_gain + right_gain
            self.ans = max(self.ans, price_path)

            return node.val + max(left_gain, right_gain)

        max_gain(root)

        return self.ans