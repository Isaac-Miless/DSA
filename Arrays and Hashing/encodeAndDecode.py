class Solution:

    def encode(self, strs: list[str]) -> str:
        # encode the list of strings into a single string
        if strs == []:
            return 'ENCODE_EMP_STR'
        return '\n'.join(strs)

    def decode(self, s: str) -> list[str]:
        # decode the string into the list of strings
        if s == 'ENCODE_EMP_STR':
            return []
        return s.split('\n')

# Time complexity: O(n)
# Space complexity: O(n)
# where n is the number of strings in the list

solution = Solution()

encoded = solution.encode([""])
decoded = solution.decode(encoded)

print(encoded)
print(decoded)
