from typing import *

class NamelessClass:
    def __init__(self):
        res = self.bs([2, 4, 6, 8, 9], 8)
        print(res)
        # O/P must be 3

    def bs(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums)-1
        while(L<R):
            M=(L+R)//2
            if nums[M] == target:
                return M
            elif nums[M] > target:
                R=M-1
            else:
                L=M+1
        return -1

obj = NamelessClass()
