class Solution(object):
    def isPalindrome(self, s):
      """
      Approach:
      iterate s and if c.isalum() then store in ss, reverse ss (rev = ss[::-1]) and check if ss==rev
      time: O(n) --- space: O(n)
      """
        ss = ""
        for c in s:
            if c.isalnum():
                ss += c.lower()

        rev = ss[  :  : -1]

        if(ss==rev):
            return True
        return False      
