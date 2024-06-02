class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool

        Approach: 
        perform dfs on possible 4 paths, by iterating every 2D board
        Time: O(r*c*dfs) ... dfs = 4^len(word) MMMMMMMMMMMMMMMMMMMMMMMM
        """
        visited = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if r>=len(board) or c>=len(board[0]) or r<0 or c<0 or board[r][c] != word[i] or (r,c) in visited:
                return False
            
            # character match
            visited.add((r,c))

            # iterate to 4x locations
            temp = (
                dfs(r+1, c, i+1) or
                dfs(r-1, c, i+1) or
                dfs(r, c+1, i+1) or
                dfs(r, c-1, i+1)
            )
            
            # clean-up crew
            visited.remove((r,c))
            return temp

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True
            
        return False
            


        
