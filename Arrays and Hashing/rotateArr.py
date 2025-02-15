class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        # --------------------------------
        # O(n) time complexity
        # O(n) space complexity
        
        # k = k % len(nums)
        # nums[:] = nums[-k:] + nums[:-k]
        # return nums
        
        # --------------------------------
        # O(n) time complexity
        # O(1) space complexity (in-place)
        
        n = len(nums)
        k %= n

        reverse(nums, 0, n-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, n-1)
        
        return nums

nums = [1,2,3,4,5,6,7]
k = 3
print(Solution().rotate(nums, k)) # [5,6,7,1,2,3,4]
