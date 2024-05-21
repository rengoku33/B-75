# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode

        Approach:
        create a dummy node and attach it before head and L,R = dummy, head... move till R hits length n, move L,R till R reaches None and now we have L one node behind target, skip the next node it inorder to drop it... finally return dummy.next (which is head)
        time: O(n) --- space: O(1)
        """

        dummy = ListNode(0, next=head)
        L = dummy
        R = head

        # move R to nth location from start
        while n>0:
            R=R.next
            n-=1
        
        # move L,R till R reaches end, now L will be one node behind target
        while R:
            R=R.next
            L=L.next 
        
        # now the next node to L is the target, skip it inorder to drop it
        L.next = L.next.next

        return dummy.next
