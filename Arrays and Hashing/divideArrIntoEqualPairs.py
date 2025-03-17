class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        oddSet = set()

        for num in nums:
            if num in oddSet:
                oddSet.remove(num)
            else: oddSet.add(num)
        
        return not oddSet
