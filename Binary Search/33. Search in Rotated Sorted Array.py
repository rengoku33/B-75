class Solution(object):
    def search(self, nums, target):
        """
        Approach:
        L and R at 0, len(nums)-1, while L<=R: calc M and check if val M == target, if we are in the left sorted area => if target is "smaller then left" or "bigger than mid" we shift to right, else we shift left => else we are in the right sorted area => # if target is "smaller then middle" or "bigger than right" we shift to left, else we shift to right... finally return -1 (target not in list)
        time: O(log n) --- space: O(n)
        """

        L, R = 0, len(nums)-1

        while L<=R:
            M = (L+R)//2
            if nums[M]==target:
                return M

            # if we are in the left sorted area
            if nums[L] <= nums[M]:
                # if target is "smaller then left" or "bigger than mid".... we shift to right
                if target<nums[L] or target>nums[M]:
                    L = M +1
                else:
                    R = M -1
            # else we are in the right sorted area
            else:
                # if target is "smaller then middle" or "bigger than right".... we shift to left
                if target<nums[M] or target>nums[R]:
                    R = M -1
                else:
                    L = M +1

        # in case value is not in the list
        return -1


