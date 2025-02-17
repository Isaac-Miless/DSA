class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # some dynamic programming solution here
        n = len(nums)
        idx = 0
        
        for i in range(n):
            if idx < i: return False
            idx = max(idx, i + nums[i])
        
        return True
        

print(Solution().canJump([2,3,1,1,4])) # True
print(Solution().canJump([3,2,1,0,4])) # False
