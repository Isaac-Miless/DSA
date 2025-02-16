class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        
        minBuy = prices[0]
        res = 0
        track = []
        
        for i, price in enumerate(prices):
            if price < minBuy:
                minBuy = price
            
            if price > minBuy:
                track.append(price - minBuy)
            
            if i > 0 and price < prices[i-1]:
                res += (max(track) if track else 0)
                track = []
                minBuy = price

        return res + (max(track) if track else 0)
    
sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4])) # 7
print(sol.maxProfit([7,6,4,3,1])) # 0
print(sol.maxProfit([1,2,3,4,5])) # 4
