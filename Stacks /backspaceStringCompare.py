class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack1 = []
        for char in s:
            if char != "#": stack1.append(char)
            elif stack1: stack1.pop()
            
        stack2 = []
        for char in t:
            if char != "#": stack2.append(char)
            elif stack2: stack2.pop()

        return stack1 == stack2
