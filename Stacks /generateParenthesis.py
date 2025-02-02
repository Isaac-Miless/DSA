class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # parenthesis = []
        # def backtrack(s = '', open = 0, close = 0):
        #     if len(s) == 2 * n:
        #         parenthesis.append(s)
        #         return
        #     if open < n:
        #         backtrack(s + '(', open + 1, close)
        #     if close < open:
        #         backtrack(s + ')', open, close + 1)
        # backtrack()
        # return parenthesis
        
        stack = []
        res = []
        
        def backtrack(openN=0, closedN=0):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
                
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
            
            backtrack()
            return res

# Given an integer n, return all well-formed
# parenthesis strings that you can generate with n
# pairs of parenthesis.

# O(n) - Stack (Backtracking)
# Explanation:
# 1. Create a stack to store the parenthesis
# 2. If the stack is empty, add an open parenthesis
# 3. If the stack is not empty, add a close parenthesis
# 4. If the stack is not empty and the number of open parenthesis is less than n, add an open parenthesis
# 5. If the stack is not empty and the number of close parenthesis is less than the number of open parenthesis, add a close parenthesis
# 6. If the number of open and close parenthesis is equal to n, add the parenthesis to the result
# 7. Return the result

# n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

