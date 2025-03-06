class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        """
        res = ""
        stack = []
        for i in range(len(pattern) + 1):
            stack.append(i + 1)
            if i == len(pattern) or pattern[i] == "I":
                while stack:
                    res += str(stack.pop())
        return res

sol = Solution()
print(sol.smallestNumber("ID"))  # "132"
print(sol.smallestNumber("DI"))  # "321"
print(sol.smallestNumber("D"))  # "21"
print(sol.smallestNumber("I"))  # "12"
print(sol.smallestNumber("IIIDIDDD"))  # "123456789"
print(sol.smallestNumber("DDDDIIII"))  # "987654321"
