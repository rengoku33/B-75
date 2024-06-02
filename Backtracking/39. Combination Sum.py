class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]

        Approach:
        dfs backtrack, if total = target: add temp-list to sett... if total>target or i out of index: return... now add current value to list recurse current element with  total + candidates[i], pop from list and recurse nxt element... finally call dfs(i=0, temp-List=[], total=0) and return sett
        
        """
        sett = []
        def dfs(i, currList, total):
            if total == target:
                sett.append(list(currList))
                return
            if total>target or i>= len(candidates):
                return
            
            currList.append(candidates[i])
            dfs(i, currList, total+candidates[i])
            currList.pop()
            dfs(i+1, currList, total)
        
        dfs(0, [], 0)
        return sett
