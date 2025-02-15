class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 2 
        
        if len(nums) <= k:
            return len(nums)
        
        for i in range(2, len(nums)):
            # if the current element is not equal to the element 2 positions behind the current element
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1

        return k

nums = [1,1,1,2,2,3]
print(Solution().removeDuplicates(nums)) # 5
