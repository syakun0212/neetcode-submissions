class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxP = 0 

        start, end = 0, 0
        while end < len(prices):
            p = prices[end] - prices[start]
            maxP = max(maxP, p)
            if prices[end] < prices[start]:
                start = end 
                
            end += 1 

        return maxP 



