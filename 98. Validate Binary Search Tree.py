# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def helper(node, low, high):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            if not helper(node.left, low, node.val):
                return False
            if not helper(node.right, node.val, high):
                return False
            return True

        return helper(root, float('-inf'), float('inf'))


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # dfs
        if not root:
            return True

        stack = [[root, float('-inf'), float('inf')]]
        while stack:
            root, low, high = stack.pop()
            if not root:
                continue
            if root.val <= low or root.val >= high:
                return False
            stack.append([root.right, root.val, high])
            stack.append([root.left, low, root.val])

        return True


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # inorder
        if not root:
            return True
        stack = []
        inorder = float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True
