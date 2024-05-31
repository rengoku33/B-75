# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Approach: 
        1) perform DFS(post) on two separate paths,
        2) check for split-sub-tree max and 
        3) return root + max(leftPath,rightRight)

        Time: O(n) --- Space: O(1)
        """

        res = [root.val]
        self.dfs(root, res)
        return res[0]

    def dfs(self, root, res):

        if not root:
            return 0

        leftPath = self.dfs(root.left, res)
        rightPath = self.dfs(root.right, res)

        leftPath = max(leftPath, 0)              # to weed out, if leftPath or rightPath has negative value
        rightPath = max(rightPath, 0)            # ""

        res[0] = max(res[0], root.val + leftPath + rightPath)    # dem splits

        return root.val + max(leftPath, rightPath)  # initially leftPath goes deep to the leftmost node and returns its value as the leftPath


