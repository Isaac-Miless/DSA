class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        
        for char in s:
            # if they're the same letter, and they're not equal (different cases)
            if stack and stack[-1].lower() == char.lower() and stack[-1] != char:
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)

sol = Solution()
print(sol.makeGood("leEeetcode"))  # "leetcode"
print(sol.makeGood("abBAcC"))  # ""
print(sol.makeGood("s"))  # "s"
