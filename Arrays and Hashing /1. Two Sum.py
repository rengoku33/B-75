class Solution(object):
    def twoSum(self, nums, target):
        """
        Approach:
        1) brute force - O(n^2)
        2) create a map and iterate through range on list and check target-current is present in map, if present return its value and current, else store in map --- time: O(n), space O(n)
        """
      
        map = {}
        for i in range(len(nums)):
            if target-nums[i] in map:
                return [map[target-nums[i]], i]
            map[nums[i]] = i
        return False 

        
