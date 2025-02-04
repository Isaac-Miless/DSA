class Solution(object):
    def maxAscendingSum(self, nums) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        currMax = 0
        stack = [0]

        for num in nums:
            if num > stack[-1]:
                currMax += num

                if currMax > res:
                    res = currMax

            else:
                stack = []
                currMax = num
            
            stack.append(num)
        
        return res

sol = Solution()
print(sol.maxAscendingSum([10,20,30,5,10,50])) # 65
print(sol.maxAscendingSum([10,20,30,40,50])) # 150
print(sol.maxAscendingSum([12,17,15,13,10,11,12])) # 33
print(sol.maxAscendingSum([100,10,1])) # 100
