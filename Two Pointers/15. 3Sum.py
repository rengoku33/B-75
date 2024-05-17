class Solution(object):
    def threeSum(self, nums):
        """
        Approach:
        sort nums, iterate nums with i and while loop i+1 and len(nums)-1 using L and R, check sum = nums[i] + nums[L] + nums[R], if yes then add to list (After checking not in list), elif sum<0 increment L, else decrement R
        time: O(n log n) + O(n2.m)  => O(n2.m) --- space: O(n)
        """

        nums.sort()
        res = []
        for i in range(len(nums)-2):
            L=i+1
            R=len(nums)-1
            while(L<R):
                sum = nums[i] + nums[L] + nums[R]
                if(sum==0):
                    ans = [nums[i], nums[L], nums[R]]
                    if ans not in res:
                        res.append(ans)
                elif(sum<0):
                    L+=1
                    continue
                R-=1
        return res
            
        
