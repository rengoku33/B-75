# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        Approach:
        create an empty sett, while head: add the node itself to head and when the node is found in sett then return true (Cycle Detected)... we run out of loop when we reach None so, return false(No Cycle)
        time: O(n) --- space: O(n)
        """
        sett = set()

        while head:
            if head in sett:
                return True

            sett.add(head)
            head=head.next

        return False
