class Solution:
    def largestRectangleArea(self,heights):
        # Optimal (Stack): O(n)
        stack = []
        maxArea = 0
        
        for idx, height in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > height:
                stackIdx, stackHeight = stack.pop()
                maxArea = max(maxArea, stackHeight * (idx-stackIdx))
                start = stackIdx
            stack.append((start, height))
        
        # extended all the way to the end of the histogram, so we still need to
        # compute their widths
        for idx, height in stack:
            maxArea = max(maxArea, height * (len(heights) - idx))
        
        return maxArea

sol = Solution()
arrIn = [7,1,7,2,2,4]
print(sol.largestRectangleArea(arrIn))


