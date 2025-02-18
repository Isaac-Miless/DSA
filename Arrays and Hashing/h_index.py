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
        
        pass

citations = [3,0,6,1,5]
sol = Solution()
print(sol.hIndex(citations)) # 3
