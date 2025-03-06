class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [] 
        ops = ("AB", "CD")
        
        for i in range(len(s)):
            stack.append(s[i])
            if len(stack) >= 2 and ''.join(stack[-2:]) in ops:
                stack = stack[:-2]
        return len(stack)
