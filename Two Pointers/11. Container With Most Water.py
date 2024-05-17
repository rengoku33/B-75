class Solution(object):
    def maxArea(self, height):
        """
        Approach:
        L and R, while(L<R) => temp-area = min(height[L], height[R]) * (R-L) and set area to max(temp-area, area), if R lower then decrement R else increment L
        time: O(n) --- space: O(n)
        """
        area=0
        L=0
        R=len(height)-1
        while(L<R):
            temp_area = min(height[L], height[R]) * (R-L)
            area= max(temp_area, area)
            if height[R]<height[L]:
                R-=1
                continue
            L+=1
        return area
