# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Approach:
1) perform dfs(pre) and make it list -> return string
2) convert string -> list and perform dfs(pre) on list with i as global var
'''
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        lst = []

        def dfs(root):
            if not root:
                lst.append('N')
                return
            
            lst.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
            return

        dfs(root)
        return ','.join(lst)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        lst = data.split(',')
        self.i=0

        def dfs():
            if lst[self.i] == 'N':
                self.i+=1
                return None
            node = TreeNode(int(lst[self.i]))
            self.i+=1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
