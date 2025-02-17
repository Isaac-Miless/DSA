class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # some dynamic programming solution here
        n = len(nums)
        memo = {}
        
        def compute(i):
            if i >= n-1: return True
            if nums[i] == 0: return False
            if i in memo: return memo[i]
            
            for j in range(i+1, min(i + nums[i], n-1)+1):
                if compute(j):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        
        return compute(0)
        

print(Solution().canJump([2,3,1,1,4])) # True
print(Solution().canJump([3,2,1,0,4])) # False
