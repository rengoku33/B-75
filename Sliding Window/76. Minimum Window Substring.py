class Solution(object):
    def minWindow(self, s, t):
        """
        Approach:
        two empty maps and transfer t to map and L at 0 and HAVE, NEED = 0, len(map1) iterate with R till len(S)... add s[R] to 2nd map, when c matches and value matches with both maps, incr HAVE... while HAVE == NEED, (update result and pop from left) calc and store the min window index [x,y], decr s[L] from map2 and decr HAVE (if in map1 and value of map2 less than map1)  and move L... finally display min window s[x,y+1] as result
        time: O(n) --- space: O(n)
        """

        if t=="": return ""                                 # Edgecase

        window, countT = {}, {}
        L=0
        resLen, res = float("infinity"), [-1,-1]            # "resLen" to calc the min window size and "res" to store the indices when min window is found

        for c in t:
            countT[c] = 1 + countT.get(c,0)                 # store t in map1

        have, need = 0, len(countT)                         # have == need when the map2 has same elements and values as map1 or more
        
        for R in range(len(s)):
            c = s[R]
            window[c] = 1 + window.get(c, 0)                # keep moving R and while moving add it to map2

            if c in countT and countT[c] == window[c]:      # when both the char and values matches with map1, then incr "have"
                have += 1
            
            while have == need:                             # have == need when the map2 has same elements and values as map1 or more
                # update the result
                if (R-L+1) < resLen:                        # update the result = when the current window is the minimum of size, set the "resLen" to window-size and assign the L and R to "res"
                    resLen = (R-L+1)
                    res = L, R
                # drop the left
                window[s[L]] -= 1                           # drop the left = decr the char at L in map2, if the removed char is in map1 and removing it caused the value of that char at map2 to be less than map1... then decr "have"
                if s[L] in countT and window[s[L]] < countT[s[L]]:
                    have -= 1
                L+=1                                        # move L

        L, R = res                                          # fetch the indices from res at some var, if res has been changed from initial declaration then return s[start:end+1]... else return empty string
        if res != float("infinity"):
            return s[L:R+1]
        else:
            return ""
                


        
