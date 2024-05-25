# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool

        Approach:
        handle edge cases first... if both are None then true, if p or q is None return False, if p.val != q.val return False... finally return (left-node-recursion-call AND right-node-recursion-call)
        time: O(p+q), len of both trees --- space: O(1)
        """
        
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
