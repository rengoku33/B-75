class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        Approach:
        1) prefix and postfix list which will multiply and store the elements accordingly, then a res list which will res[i] = prefix[i-1] * pstfix[i+1]
        time --- O(n+n+n) = O(n)

        2) same approach but we lose the prefix and postfix list and perform ops on the res list, --- better space + time --- O(n+n) = O(n)
        """
        prefix = [1] * len(nums)
        pstfix = [1] * len(nums)
        
        for i in range(0, len(nums), 1):               # build the prefix list
            if i==0:
                prefix[i] = nums[i]
                continue
            prefix[i] = prefix[i-1] * nums[i]
        
        for i in range(len(nums)-1, 0, -1):            # build the postfix list
            if i==len(nums)-1:
                pstfix[i] = nums[i]
                continue
            pstfix[i] = pstfix[i+1] * nums[i]

        res = [1] * len(nums)

        for i in range(len(nums)):                      # handle edgecases and build res list
            if i==0:                                  
                res[i] = pstfix[i+1]
                continue
            if i==len(nums)-1:
                res[i] = prefix[i-1]
                continue 
            res[i] = prefix[i-1] * pstfix[i+1]          

        return res

  #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    

        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]           # 1 1 2 6

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]          # 24 12 8 6 <-

        return res
