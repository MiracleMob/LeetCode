# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.ans(root, res)
        return res

    def ans(self, root, res):
        if root:
            if root.left:
                self.ans(root.left, res)
            res.append(root.val)
            if root.right:
                self.ans(root.right, res)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        ans = []
        tmp = root
        while tmp or len(stack) > 0:
            while (tmp):
                stack.append(tmp)
                tmp = tmp.left

            tmp = stack.pop()
            ans.append(tmp.val)
            tmp = tmp.right

        return ans











