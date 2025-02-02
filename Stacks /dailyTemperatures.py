class Solution:
    def dailyTemperatures(self,temperatures):
        stack = [] # pairs, temp, idx
        res = [0] * len(temperatures)
        
        # Optimal (Stack): O(n)
        for idx, elem in enumerate(temperatures):
            while stack and elem > stack[-1][0]:
                _, stackIdx = stack.pop()
                res[stackIdx] = idx - stackIdx
            
            stack.append((elem, idx))
        return res

sol = Solution()
arrIn = [30,38,30,36,35,40,28]
# arrIn = [22,21,20]
print(sol.dailyTemperatures(arrIn))

# Explanation
# Init a stack to store tuples of temperatures and their indexes and res array
# Enumerate the input array to get elements and their indexes,
# For each pair, while the stack is not empty and the current elem is greater than the top of the stack (elem)
# Init stackTemp and stackIdx from the top of the stack
# Set that position in the result array to be the difference in indexes
# If no solution is found, don't update the res array, and instead add the pair to the stack

# Test Cases
# Input: temperatures = [30,38,30,36,35,40,28]
# Output: [1,4,1,2,1,0,0]

# Input: temperatures = [22,21,20]
# Output: [0,0,0]
