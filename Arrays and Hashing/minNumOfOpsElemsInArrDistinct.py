class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = [0] * 101 # because the max value of nums[i] = 100

        for i in reversed(range(len(nums))):
            counts[nums[i]] += 1
            # to remove 3 elems from start it's 1 operation,
            # to remove 6 elems, it's 2 operations, and so on
            # this is what the formula below is doing
            if counts[nums[i]] == 2: return (i + 3) // 3

        return 0 # if a duplicate is never found return 0
