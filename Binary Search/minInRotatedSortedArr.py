class Solution:
    def findMin(self, nums: list[int]) -> int:
        l,r = 0, len(nums)-1
        
        while l < r:
            mid = (l+r)//2
            # if mid is greater than the last element, then the minimum
            # element is to the right of mid
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
    
sol = Solution()
nums = [3,4,5,1,2]
print(sol.findMin(nums)) # 1
