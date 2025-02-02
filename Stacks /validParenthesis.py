class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketMap = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for char in s:
            if char not in bracketMap:
                stack.append(char)
                continue
            
            if not stack or stack[-1] !=  bracketMap[char]: return False
            stack.pop()

        # if stack is empty, return True
        return not stack

# Optimal: O(n)
# loop through Input: s = "([{}])"
# add elements to the stack
# if the element is a closing bracket, pop the stack and check if it's the correct opening bracket
# if not, return False
