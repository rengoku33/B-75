# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        Approach:
        simply traverse the tree in pre-order if root: store on temp and switch nodes, then self.invertTree(root.left), self.invertTree(root.right)... finally return root
        time: O(n) --- space: O(1)
        """
        if root:
            temp = root.left
            root.left = root.right
            root.right = temp

            self.invertTree(root.left)
            self.invertTree(root.right)

        return root
