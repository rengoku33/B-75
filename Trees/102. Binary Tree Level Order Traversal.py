# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        Approach:
        create queue and init with root, while queue: iterate in range of curr-queue-len, popleft and store it, if popped node contains left or right node, add them to q
        Time: O(n) --- Space: O(1)
        """
        res = []
        q = collections.deque()
        if root:
            q.append(root)

        while q:
            lust = []
            currQlen = len(q)

            for i in range(currQlen):
                node = q.popleft()
                lust.append(node.val) 

                if node.left:
                    q.append(node.left)
            
                if node.right:
                    q.append(node.right)
            res.append(lust)

        return res
