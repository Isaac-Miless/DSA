class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        less = []
        p = []
        greater = []

        for num in nums:
            if num == pivot: p.append(num)
            elif num > pivot: greater.append(num)
            else: less.append(num)

        return less + p + greater
