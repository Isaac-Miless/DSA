class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        # syms = ["+", "-", "*", "/"]
        syms = {
            "+": lambda x,y: x+y,
            "-": lambda x,y: x-y,
            "*": lambda x,y: x*y,
            "/": lambda x,y: int(x/y)
        }

        for i in tokens:
            if i in syms:
                num2 = stack.pop()
                num1 = stack.pop()
            
                stack.append(syms[i](num1, num2))
            else:
                stack.append(int(i))

        return stack[-1]

    # 5

sol = Solution()
summ = sol.evalRPN(["4","13","5","/","+"])
print(summ)
# O(n)
# If the current iter isn't in syms (it's a number), add it to the stack
# Else do the eval, and replace the stack to hold the single sum
