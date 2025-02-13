class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums[:] = [num for num in nums if num != val]
        return len(nums)

nums = [3,2,2,3]
val = 3
Solution().removeElement(nums, val)
