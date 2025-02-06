class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        productCount = {}
        count = 0
        
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]: continue
                product = nums[i] * nums[j]
                count += productCount.get(product, 0)
                productCount[product] = productCount.get(product, 0) + 1
        
        return count * 8

sol = Solution()
inp = [2,3,4,6]
print(sol.tupleSameProduct(inp)) # 8
inp = [1,2,4,5,10]
print(sol.tupleSameProduct(inp)) # 16
