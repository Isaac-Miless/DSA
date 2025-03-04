class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        result = ""
        
        for char in s:
            if char == "(":
                if stack: result += char
                stack.append(char)
            else:
                stack.pop()
                if stack: result += char
            
        return result
