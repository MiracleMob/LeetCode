# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        while root:
            if not root.left:
                # 左子树为空，找下个结点
                root = root.right
            else:
                pre = root.left
                while pre.right:
                    # 找到左子树最右结点
                    pre = pre.right

                pre.right = root.right
                root.right = root.left
                root.left = None
                # 左子树为空，找下个结点
                root = root.right





