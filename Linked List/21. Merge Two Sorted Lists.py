# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]

        Approach:
        create a dummy node and initialize list, {dummy=ListNode(), tail=dummy} while l1 and l2: compare both the values and add the node with the smaller value to new list, set l1=l1.next or l2=l2.next to iterate both the list, and tail = tail.next.. finally in case one list is empty but other list isnt, add the remaining to our tail list and return dummy.next
        time: O(n) --- space: O(n)
        """
        dummy = ListNode()              # purpose of dummy node: easy to return (ex: dummy.next) and handles edge case when both the list are empty
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next=list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next
