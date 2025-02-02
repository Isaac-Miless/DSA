class Solution:
    def trap(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        lMax, rMax, waterTrapped = 0, 0, 0

        while l < r:
            if height[l] <= height[r]:
                if height[l] < lMax: waterTrapped += lMax - height[l]
                else: lMax = height[l]
                l += 1
            else:
                if height[r] < rMax: waterTrapped += rMax - height[r]
                else: rMax = height[r]
                r -= 1
        
        return waterTrapped
            

# Brute Force: O(n^2)
# Loop through the array and for each element, find the maximum height on the left and right side of the element.
# The amount of water that can be trapped at that element is the minimum of the two maximum heights minus the height of the element.
# Add the amount of water that can be trapped at that element to the total amount of water trapped.
# Return the total amount of water trapped.

# Two Pointer, optimal solution O(n)
# Initialize two pointers, one at the left (l) and one at the right (r).
# Keep track of the maximum height seen so far from the left (lMax) and the right (rMax).
# Move the pointer that has the lower height, because the amount of water trapped is determined by the shorter wall.
# At each step, calculate the trapped water by subtracting the current height from the maximum height on that side.
# Update the maximum height for the left or right side as you move the pointers inward.
# Continue until the two pointers meet.
