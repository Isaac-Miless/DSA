class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l,r = i+1, n-1
            
            while l < r:
                numSum = nums[i] + nums[l] + nums[r]

                if numSum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    
                    while l < r and nums[l] == nums[l+1]: l += 1
                    while l < r and nums[r] == nums[r-1]: r -= 1
                    
                    l += 1
                    r -= 1
                
                elif numSum < 0: l += 1
                else: r -= 1

        return res

sol = Solution()
inp = [-1,0,1,2,-1,-4]
threeSum = sol.threeSum(inp)
print(threeSum)
