class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Approach:
        convert list to set, iterate and check if this is the starting element of a consecutive sequence, if yes then set length to 0 and keep looking for next ele with while loop and set max as max(length, longest)
        time --- O(n)?, space --- O(n)
        """

        sett = set(nums)     # searching is O(1) in set cuz it utilizes hashing
        longest = 0

        for n in nums:
            # check if this is the starting element of a consecutive sequence, else move to next element
            if (n-1) not in sett:
                length = 0
                # keep looking for the Longest Consecutive Sequence from the start of the sequence
                while (n+length) in sett:
                    length+=1
                # set the longest var to check and store the max value on every iteration
                longest = max(length, longest)
        return longest
