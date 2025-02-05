class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # calculate the next number in cycle
        def nextNum(num):
            return sum(int(digit)**2 for digit in str(num))
        
        seenNumbers = set()
        while n != 1 and n not in seenNumbers:
            seenNumbers.add(n)
            n = nextNum(n)
        
        # exits while loop once it finds a cycle or if it equals 1
        return n == 1
        
sol = Solution()
print(sol.isHappy(19))
print(sol.isHappy(2))
