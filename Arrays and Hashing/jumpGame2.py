class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # JUMP GAME 1
        # n = len(nums)
        # idx = 0
        
        # for i in range(n):
        #     if idx < i: return False
        #     idx = max(idx, i + nums[i])
        
        # return True
        
        if len(nums) <= 1: return 0
        
        n = len(nums)
        idx = 0
        steps = 0

        for i in range(n):
            for j in range(0,nums[i]+1):
                idx = max(idx, i + j)
            steps += 1
            if idx >= n-1: return steps
        
        return steps

print(Solution().jump([2,3,1,1,4])) # 2
print(Solution().jump([2,3,0,1,4])) # 2
print(Solution().jump([[1,2,1,1,1]])) # 3
