from collections import Counter, OrderedDict
class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        dic = OrderedDict()
        res = []
        color_count = Counter()

        for ball, colour in queries:
            if ball in dic:
                old_colour = dic[ball]
                color_count[old_colour] -= 1
                if color_count[old_colour] == 0:
                    del color_count[old_colour]
            dic[ball] = colour
            color_count[colour] += 1

            if len(dic) > limit:
                _, firstCol = dic.popitem(last=False)
                color_count[firstCol] -= 1
                if color_count[firstCol] == 0:
                    del color_count[firstCol]
                    
            res.append(len(color_count))
                
        return res

limit = 4
queries = [[1,4],[2,5],[1,3],[3,4]]
print(Solution().queryResults(limit, queries)) # [1, 2, 2, 3]

queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]
print(Solution().queryResults(limit, queries)) # [1, 2, 2, 3, 4]

queries = [[0,1],[1,4],[1,1],[1,4],[1,1]]
print(Solution().queryResults(limit, queries)) # [1, 2, 1, 2, 1]
