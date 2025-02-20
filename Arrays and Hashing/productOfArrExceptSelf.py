class Solution:
    def productExceptSelf(self, nums):        
        # brute force O(n^2)
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if j == i:
        #             continue
        #         res[i] *= nums[j]

        # prefix arr
        
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

print(Solution().productExceptSelf([1,2,3,4]))
