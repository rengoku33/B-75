class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        Approach:
        L and R at 0, keep moving R, while s[R] in sett: keep removing and moving s[L] in sett no dupe... add s[R] to set and set max      
        time: O(n) --- space: O(n) 
        """
        sett= set()
        longest = 0
        L=0

        for R in range(len(s)):
            while s[R] in sett:
                sett.remove(s[L])
                L+=1
            sett.add(s[R])
            longest = max(longest, (R-L+1))
        return longest
        
        
