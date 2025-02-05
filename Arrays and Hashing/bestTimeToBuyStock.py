class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices: return 0
        
        res = 0
        minBuy = prices[0]
        
        for price in prices:
            if price < minBuy:
                minBuy = price
            else:
                res = max(res, price - minBuy)

        return res
    
sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4])) # 5
print(sol.maxProfit([7,6,4,3,1])) # 0
