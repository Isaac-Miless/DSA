class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        left, right = 1, max(candies)
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            children_count = sum(pile // mid for pile in candies)
            
            if children_count >= k:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return result
    
# Time complexity: O(nlogn)
# Space complexity: O(1)


sol = Solution()
print(sol.maximumCandies([2,3,5,1,3], 3)) # 5
print(sol.maximumCandies([4,2,1,1,2], 1)) # 4
print(sol.maximumCandies([12,1,12], 10)) # 12
print(sol.maximumCandies([7,2,5,10,8], 2)) # 8
print(sol.maximumCandies([4,1,1], 2)) # 1
print(sol.maximumCandies([2,8,7], 2)) # 8
