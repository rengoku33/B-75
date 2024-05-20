class Solution(object):
    def findMin(self, nums):
        """
        Approach:
        init low at nums[0] and L and R at 0, len(nums)-1, while L<=R: if nums[L]<nums[R], we are in a undivided list, so return min(low, nums[L]), M=(L+R)//2 and check min with low, if value of L is less than M then we are in left sorted area... so shift L to M + 1, else we are in right sorted area... so shift R to M - 1... finally return low
        time: O(log n) --- space: O(n) 
        """
        low = nums[0]
        L, R = 0, len(nums)-1

        while L<=R:
            # we have reached a undivided sorted area
            if nums[L]<nums[R]:
                low =min(low,nums[L])
                break

            M = (L+R)//2
            low = min(low,nums[M])

            # if we are in left sorted area, so shift right
            if nums[L]<=nums[M]:
                L = M + 1
            # else we are in right sorted area, so shift left
            else:
                R = M - 1
        
        return low


        
