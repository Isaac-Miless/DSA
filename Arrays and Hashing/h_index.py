class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        citations.sort()
        
        # published at least x number of papers with x citations
        # h-index is the largest x

        for i in range(n):
            if citations[i] >= n-i:
                return n-i
        return 0

citations = [3,0,6,1,5]
sol = Solution()
print(sol.hIndex(citations)) # 3
