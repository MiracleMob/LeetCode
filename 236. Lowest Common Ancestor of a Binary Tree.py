# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = 0

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        def reverse(root):
            if not root:
                return False

            left = reverse(root.left)
            right = reverse(root.right)
            mid = (root == p or root == q)
            if mid + left + right >= 2:
                self.ans = root

            return mid or left or right

        reverse(root)
        return self.ans


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        stack = []
        stack.append(root)
        parent = {root: None}

        # 将p,q的父节点加入字典
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                parent[node.left] = node
            if node.right:
                stack.append(node.right)
                parent[node.right] = node
        ane = set()

        while p:
            ane.add(p)
            p = parent[p]

        while q not in ane:
            q = parent[q]

        return q

