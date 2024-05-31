# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        Approach:
        create a helper fn and pass in root, -inf, inf... in helper fn, if node is None: return True, if 'not' node.val is more than left and lesser than right: return false... recursively return (leftnode and rightnode)]
        Time: o(n) --- Space: o(1)
        """
        if root:
            return self.isValidNode(root, float('-inf'), float('inf')) 
    
    def isValidNode(self, node, left, right):
        if node is None:
            return True
        if not (node.val<right and node.val>left):
            return False
        return (self.isValidNode(node.left, left, node.val) and self.isValidNode(node.right, node.val, right))
