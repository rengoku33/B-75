# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        
        Approach:
        while len(lists)>1: create mergedlists = [], iterate the outer list by incr 2, each iteration merge i and i+1, store each iteration in merged list... convert lists = mergedlists and finally return lists[0]
        time: O(n log k), k = no of elements in lists (reduces on each iteration) and n = merge2SortedList --- space = O(n)
        """
        # edgecase: empty list or list of length 0
        if not lists or len(lists)==0:
            return None
        
        while len(lists)>1:
            mergedlists = []

            for i in range(0, len(lists), 2):                    # we are incrementing by 2, cuz each iteration we work on i, i+1
                l1 = lists[i]
                l2 = lists[i+1] if (i+1)<len(lists) else None    # if i+1 is valid index then we assign, else we work with none
                mergedlists.append(self.merge2SortedList(l1, l2))# call merge2sorted list fn on merged list 
            lists = mergedlists
        return lists[0]

    def merge2SortedList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1=l1.next
            else:
                tail.next=l2
                l2=l2.next
            tail=tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next

