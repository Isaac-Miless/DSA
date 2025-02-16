class Solution(object):
    def punishmentNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # --------------------------------
        # O(n) time complexity
        # O(1) space complexity
        res = 0
        
        # def getPunishment(i):
        #     sqr = i * i
        #     sqrCopy = sqr
        #     sumOfDigits = 0
            
        #     while sqrCopy:
        #         sumOfDigits += sqrCopy % 10
        #         sqrCopy //= 10
            
        #     if sumOfDigits == i:
        #         return sqr
        
        #     return 0

        # for i in range(1, n+1):
        #     res += getPunishment(i)
        
        # return res
        
        def canPartition(num: str, index: int, target: int) -> bool:
            if index == len(num):
                return target == 0

            sum_val = 0
            for i in range(index, len(num)):
                sum_val = sum_val * 10 + int(num[i])
                if sum_val > target:
                    break
                if canPartition(num, i + 1, target - sum_val):
                    return True
            return False

        return sum(i * i for i in range(1, n + 1) if canPartition(str(i * i), 0, i))

print(Solution().punishmentNumber(10)) # 182
