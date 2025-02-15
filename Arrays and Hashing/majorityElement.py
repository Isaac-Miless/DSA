class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max([(nums.count(i), i) for i in set(nums)])[1]

