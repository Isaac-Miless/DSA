class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        adjustedString = []
        for char in s:
            if char.isdigit():
                if adjustedString: adjustedString.pop()
            else: adjustedString.append(char)
        return "".join(adjustedString)

print(Solution().clearDigits("abc"))  # "abc"
print(Solution().clearDigits("cb34"))  # ""
print(Solution().clearDigits("ag3"))  # "a"
