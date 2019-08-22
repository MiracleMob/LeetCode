# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dp(self, cur):
        if not cur:
            return [0, 0]

        left = self.dp(cur.left)
        right = self.dp(cur.right)

        return [max(left) + max(right), cur.val + left[0] + right[0]]

    def rob(self, root: TreeNode) -> int:
        # dp[0] = 不选 dp[1] = 选
        return max(self.dp(root))