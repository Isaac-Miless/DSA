class Solution:
    def binarySearch(self, nums, target):
        if not nums: return -1
        if target < nums[0] or target > nums[-1]: return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                print(mid)
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
sol = Solution()
binInput = [-1,0,2,4,6,8]
sol.binarySearch(binInput, 4)
