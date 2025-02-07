from collections import Counter
class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        res = []
        ball_map = {}  
        color_freq = Counter()  

        for ball, color in queries:
            if ball in ball_map:
                old_color = ball_map[ball]
                color_freq[old_color] -= 1
                if color_freq[old_color] == 0:
                    del color_freq[old_color]  

            ball_map[ball] = color
            color_freq[color] += 1

            res.append(len(color_freq))

        return res
    
    # def queryResults(self, limit, queries):
    #     """
    #     :type limit: int
    #     :type queries: List[List[int]]
    #     :rtype: List[int]
    #     """
    #     dic = OrderedDict()
    #     res = []
    #     distinct = set()

    #     for ball, colour in queries:
    #         if ball in dic:
    #             if dic[ball] in distinct:
    #                 distinct.remove(dic[ball])
    #         dic[ball] = colour
    #         distinct.add(colour)

    #         if len(dic) > limit:
    #             _, firstCol = dic.popitem(last=False)
    #             if firstCol not in dic.values():
    #                 distinct.remove(firstCol)
    #         res.append(len(distinct))
                
    #     return res

limit = 4
queries = [[1,4],[2,5],[1,3],[3,4]]
print(Solution().queryResults(limit, queries)) # [1, 2, 2, 3]

queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]
print(Solution().queryResults(limit, queries)) # [1, 2, 2, 3, 4]

queries = [[0,1],[1,4],[1,1],[1,4],[1,1]]
print(Solution().queryResults(limit, queries)) # [1, 2, 1, 2, 1]

