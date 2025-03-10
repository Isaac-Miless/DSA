class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # Ensure A is the shorter array
        if len(B) < len(A):
            A, B = B, A

        # Binary search
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            # god knows what's going on here
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1



# You are given two integer arrays nums1 and nums2 of size m and n respectively, where each is sorted in ascending order. Return the median value among all elements of the two arrays.
# O(log(m + n)) time complexity
