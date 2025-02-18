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
        
        res, curr, furthest = 0, 0, 0
        for i in range(len(nums) - 1):
            furthest = max(furthest, i + nums[i])
            if i == curr:
                res += 1
                curr = furthest
        return res

print(Solution().jump([2,3,1,1,4])) # 2
print(Solution().jump([2,3,0,1,4])) # 2
print(Solution().jump([[1,2,1,1,1]])) # 3
