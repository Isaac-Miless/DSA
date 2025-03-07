class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def backtrack(index, path):
            if index == len(nums):
                self.res += path
                return
            backtrack(index + 1, path ^ nums[index])
            backtrack(index + 1, path)
        
        self.res = 0
        backtrack(0, 0)
        return self.res
