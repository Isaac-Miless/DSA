class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        n = len(nums[0])
        res = ["0"] * n
        nums = set(nums)

        for i in range(n):
            if "".join(res) in nums: res[i] = "1"

        return "".join(res)
