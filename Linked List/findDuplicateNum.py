class Solution(object):
    def findDuplicate(self, nums: list[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # can't modify array
        # must be O(1) space
        # must be O(n) time
        
        # Brute Force (not optimal) (O(n) space and time)
        # hashSet = set()
        # for num in nums:
        #     if num in hashSet:
        #         return num
        #     hashSet.append(num)
        
        # return -1
        
        # Optimal Solution (O(n) time O(1) space)
        # for i in range(len(nums)):
        #     if (nums[i] * -1) in nums: return nums[i]
        #     nums[i] *= -1
        
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0: return abs(num)
            nums[idx] *= -1
        
        return -1
        

nums = [1,3,4,2,2]
print(Solution().findDuplicate(nums)) # 2

nums = [3,1,3,4,2]
print(Solution().findDuplicate(nums)) # 3

nums = [3,3,3,3,3]
print(Solution().findDuplicate(nums)) # 3
