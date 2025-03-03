class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        maxDepth = 0
        
        for char in s:
            if char == "(":
                stack.append(char)
                maxDepth = max(maxDepth, len(stack))
            elif char == ")":
                stack.pop()
        
        return maxDepth
