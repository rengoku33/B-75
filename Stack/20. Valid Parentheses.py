class Solution(object):
    def isValid(self, s):
        """
        Approach:
        map closing with opening and iterate through s, if any closing tag => if stack not empty and at top of stack => pop... else return false else add to stack (opening tag)... finally return true if stack is empty, else return false
        time: O(n) --- space: O(n)
        """
        
        stac = []
        closer = {")":"(",  "}":"{",  "]":"["}

        for c in s:
            if c in closer:
                if stac and stac[-1] == closer[c]:
                    stac.pop()
                else:
                    return False
            else:
                stac.append(c)
        return True  if not stac else False
