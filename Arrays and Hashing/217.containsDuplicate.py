class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        Approaches:
        1) Iterate through the list and check with every other item --- time: O(n^2) space: O(1)
        2) Sort the list and iterate through to see if the nxt element is same --- time: O(n log n) space: O(1)
        3) Check if present in hashmap and if not insert --- time: O(n) space: O(n)
        
        """

        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
