# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int'
        Approach:
        inOrder traverse the tree and store val in a list, return list[k-1]
        Time: O(n) --- Space: O(n)
        """

        treelist = []
        self.inOrder(root, treelist)

        return treelist[k-1]

    
    def inOrder(self, node, treelist):
        if node:
            self.inOrder(node.left, treelist)
            treelist.append(node.val)
            self.inOrder(node.right, treelist)
