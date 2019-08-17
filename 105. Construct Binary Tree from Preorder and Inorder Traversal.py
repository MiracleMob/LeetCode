# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:inorder.index(preorder[0]) + 1],
                                   inorder[0:inorder.index(preorder[0])])
        root.right = self.buildTree(preorder[inorder.index(preorder[0]) + 1:],
                                    inorder[inorder.index(preorder[0]) + 1:])

        return root
