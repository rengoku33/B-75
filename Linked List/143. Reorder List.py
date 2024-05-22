# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.

        Approach:
        1)Iterate and store node itself in arr... 2)L, R = 0,len(arr)-1 While L<R: set the pointer of array of node (L to R) $ incr L then (R to L) & incr R... 3)Finally set the pointer of last node to None to prevent cycle (arr[L].next = None)        
        """
        # if head is null, we return NOTHING
        if not head:
            return

        # Step 1: store every node* itself in an array
        arr = []
        curr = head
        while curr:
            arr.append(curr)
            curr=curr.next
      
        # Step 2: reorder nodes with array elements (since each array element is a node)
        L,R = 0, len(arr)-1
        while L<R:
            arr[L].next = arr[R]
            L+=1
            arr[R].next = arr[L]
            R-=1

        # Step 3: Ensure the last node points to None (prevents cycle)
        arr[L].next = None
        
      
