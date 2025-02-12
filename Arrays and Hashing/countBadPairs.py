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
        
        # number of total pairs are: n (n-1) // 2

        map = {}
        good = 0
        
        for i in range(len(nums)):
            good += map.get(nums[i] - i, 0)
            map[nums[i] - i] = map.get(nums[i] - i, 0) + 1
            
        n = len(nums)
        return (n * (n-1) // 2) - good
            
            
            

# Keep a counter of nums[i] - i in a HashMap
# (j - i != nums[j] - nums[i]) === (nums[i] - i != nums[j] - j).
print(Solution().countBadPairs([4,1,3,3]))

# Explanation: The pair (0, 1) is a bad pair since 1 - 0 != 1 - 4.
# The pair (0, 2) is a bad pair since 2 - 0 != 3 - 4, 2 != -1.
# The pair (0, 3) is a bad pair since 3 - 0 != 3 - 4, 3 != -1.
# The pair (1, 2) is a bad pair since 2 - 1 != 3 - 1, 1 != 2.
# The pair (2, 3) is a bad pair since 3 - 2 != 3 - 3, 1 != 0.
# There are a total of 5 bad pairs, so we return 5.

print(Solution().countBadPairs([1,2,3,4,5])) # 0
