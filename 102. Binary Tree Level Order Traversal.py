# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = []
        ans = []
        if not root:
            return ans
        queue.append(root)
        level_length = 1
        level = 0
        while queue:
            level_length = len(queue)
            ans.append([])
            for i in range(level_length):
                t = queue.pop(0)
                ans[level].append(t.val)
                if t.left:
                    queue.append(t.left)
                if t.right:
                    queue.append(t.right)

            level += 1

        return ans

