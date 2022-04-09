############### prob link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 1 :
            return 0
        min = prices[0]; r= 0
        for i in prices:
            if i < min:
                min = i
            r = max(r, i - min)
        return r
                
