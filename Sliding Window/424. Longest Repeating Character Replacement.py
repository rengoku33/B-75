class Solution(object):
    def characterReplacement(self, s, k):
        """
        Approach:
        Create an empty map and L at 0, iterate with R from 0 to len(s)... add char s[R] to map on each move, while length-of-window - most-frequent-value > K (non-repetitions exceeds K) decr s[L] from map and move L, finally calculate the max length of window
        time: O(n) --- space: O(n)
        """
        L=0
        longest=0
        count = {}

        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)            # add char to map by moving R

            while (R-L+1) - max(count.values()) > k:        # if length-of-window - most-frequent-value > K (non-repetitions must be <= K)
                count[s[L]] -= 1                            # remove left most element of s from map   
                L+=1                                        # move left pointer

            longest = max(longest, (R-L+1))                 # set the longest to the size of maximum window with repeating char
        
        return longest
