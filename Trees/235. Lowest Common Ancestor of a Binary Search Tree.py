# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        Approach:
        If root is not null: if p,q value is smaller than root.val -> recurse root.right, elif p,q value is smaller than root.val -> recurse root.left... else return root
        Time: O(log n) n = no of nudes --- Space: o(1)
        """
        if root:
            if root.val<p.val and root.val<q.val:
                return self.lowestCommonAncestor(root.right, p, q)
            elif root.val>p.val and root.val>q.val:
                return self.lowestCommonAncestor(root.left, p, q)
            else:
                return root
