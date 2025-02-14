class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = [num for i, num in enumerate(nums) if i == 0 or num != nums[i-1]]
        return len(nums)
