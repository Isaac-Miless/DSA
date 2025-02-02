class Solution:
    def maxArea(self, heights: list[int]) -> int:
        l, r = 0, len(heights) - 1
        maxCapacity = 0
        while l < r:
            capacity = min(heights[l], heights[r]) * (r - l)
            maxCapacity = max(maxCapacity, capacity)
            
            # print(f"{l}: {heights[l]}")
            # print(f"{r}: {heights[r]}")
            # print(capacity)
            # print("-----")
            
            if heights[l] < heights[r]: l += 1
            else: r -= 1

        return max(capacities)


# Working out Capacity

# height of smaller element (can't slant)
# width of the difference of idx's

# 7 * abs(1 - 5) = 28
# 6 * abs(1 - 7) = 36

# Brute Force: O(n^2)
# Iterate through all possibilities and their capacities, return the max

# Two Pointer, Optimal: O(n)
# Two pointers, left and right
# Calculate the capacity of the two pointers
# Move the pointer with the smaller height inwards
# Continue until the pointers meet
# Return the max capacity
