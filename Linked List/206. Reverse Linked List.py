# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        Approach:
        create two nodes - prev, curr = None, head... while curr: temp = (1) curr.next, (2) curr.next = prev, (3) prev = curr, (4) curr = temp... finally return prev (which is now the head)
        time: O(n) --- space: O(1)
        """
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev
        
