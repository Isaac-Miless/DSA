class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = [-1] * len(nums1)
        for num in nums1:
            if num not in nums2: return -1
            idx = nums2.index(num)
            for i in range(idx, len(nums2)):
                if num < nums2[i]:
                    res[nums1.index(num)] = nums2[i]
                    break
        
        return res
