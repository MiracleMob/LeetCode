# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def helper(root, string):
            if not root:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = helper(root.left, string)
                string = helper(root.right, string)
            return string

        return helper(root, '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def helper_(data_list):
            if data_list[0] == 'None':
                data_list.pop(0)
                return None
            root = TreeNode(data_list[0])
            data_list.pop(0)
            root.left = helper_(data_list)
            root.right = helper_(data_list)

            return root

        data_list = data.split(',')
        root = helper_(data_list)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))