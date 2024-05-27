# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        Approach:
        Traverse the main tree(DFS) and perform same tree alogrithm on each node of main tree, edge case... if not subRoot: True, if not root: False
        Time: O(R.S) --- Space: O(1)
        """
        if not subRoot:
            return True
        if not root:
            return False
        

        if self.sameTree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)) # why 'or' on DFS?

    def sameTree(self, R, S):
        if not R and not S:
            return True

        if R and S and R.val == S.val:
            return (self.sameTree(R.left, S.left) and self.sameTree(R.right, S.right)) 

        return False
