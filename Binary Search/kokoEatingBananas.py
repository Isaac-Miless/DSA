import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # have to eat all piles (len(piles)) in h hours
        # brute force is to start at speed 1, and see if 
        # we can eat all piles in h hours. If not, then
        # increment speed by 1 and try again.
        # This is O(max(piles) * p) time complexity
        # Binary search can be used to reduce time complexity
        # to O(log(max(piles)) * p) which reduces it slightly
        
        # minimum speed is 1 (otherwise not eating)
        # maximum speed is max(piles) (can do the biggest pile in 1 hour)
        l,r = 1, max(piles)
        res = r 
        
        while l <= r:
            k = (l+r)//2
            totalTime = 0
    
            for p in piles:
                # add the time it takes to eat the pile at speed k
                totalTime += math.ceil(float(p)/k)
            
            # if we can eat all piles in h hours, then we can try to eat slower
            # otherwise we need to eat faster
            if totalTime <= h:
                res, r = k, k-1
            else: l = k+1
        return res
 
sol = Solution()
print(sol.minEatingSpeed([1,4,3,2], 9)) # 2
