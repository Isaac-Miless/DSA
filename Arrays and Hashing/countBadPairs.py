class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n^2) -- too slow
        # badPairs = 0
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] > nums[j] and i < j:
        #             badPairs += 1
        # return badPairs

# Keep a counter of nums[i] - i in a HashMap
