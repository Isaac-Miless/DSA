class Solution:
        def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
            # below is a one-pass solution, O(log(rows*cols)) time complexity
            # however it can be done with 2 passes which is a bit simpler
            # but O(log(rows) + log(cols)) time complexity
            
            if not matrix: return False
            
            rows, cols = len(matrix), len(matrix[0])
            # treats it as a 1D array
            left, right = 0, rows * cols - 1
            
            while left <= right:
                # gets the index of the absolute middle element
                mid = (left + right) // 2
                # maps it back to 2D array, for example if mid = 5 (zero-index), then
                # mid // cols = 1, mid % cols = 1
                midElement = matrix[mid // cols][mid % cols]
                if midElement == target:
                    return True
                elif midElement < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return False
        
sol = Solution()
matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]

# [1,2,4,8]
# [10,11,12,13]
# [14,20,30,40]

target = 10
print(sol.searchMatrix(matrix, target))
