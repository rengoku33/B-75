class Solution(object):
    def isAnagram(self, s, t):
        """
        total count of each character in string s must be equal to that of string t = valid anagram
        Approach: 
        1) iterate and store char count of 2 strings in 2 separate maps, compare both maps --- time: O(n) or O(s or t), space: O(n) or O(s + t) 
        """
        if len(s) != len(t):                        # if the length are not equal, which means the characters are not aswell, so we eliminate the edge case
            return False
        
        map1, map2 = {}, {}                         # declare 2 empty hashmaps

        for i in range(len(s)):                     # start:i=0 stop:i<len(s)
            map1[s[i]] = 1 + map1.get(s[i], 0)      # we are storing char as key and int as value
            map2[t[i]] = 1 + map2.get(t[i], 0)      # so we check if the char is present in map, if present we increment, else we get default=0 and set it to +1 and make new element
        
        if map1==map2:                              # compare both maps
            return True

        return False

            

        
