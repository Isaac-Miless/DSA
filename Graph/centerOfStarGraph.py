class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        firstEdge = edges[0]

        if firstEdge[0] in edges[-1]: return firstEdge[0]
        else: return firstEdge[1]
