class Solution(object):
    def maxProfit(self, prices):
        """
        Approach:
        L and R at 0, while R<len(prices): if L value is smaller than R value, calc profit = max(profit, prices[R]-prices[L])... else shift L=R and finally incr R
        time: O(n) --- space: O(1)
        """
        L, R = 0 , 1
        profit=0

        while R<len(prices):
            if prices[L]<prices[R]:
                profit = max(profit, prices[R]-prices[L])
            else:
                L=R
            R+=1
        return profit

        
