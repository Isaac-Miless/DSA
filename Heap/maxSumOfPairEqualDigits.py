class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def getSumOfDigits(num):
            sumOfDigits = 0
            while num > 1:
                sumOfDigits += num % 10
                num //= 10
            return sumOfDigits
        
        pass
