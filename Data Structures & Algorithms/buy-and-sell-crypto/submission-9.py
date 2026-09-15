class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxP = 0 
        start, end = 0, 0

        while end < len(prices):
            if prices[end] > prices[start]:
                diff = prices[end] - prices[start]
                maxP = max(maxP, diff)
            else:
                start = end 

            end += 1 
            
        return maxP 



