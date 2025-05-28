class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        # res = []
        
        # for i, word in enumerate(words):
        #     if x in word:
        #         res.append(i)
                
        # return res
        
        return [i for i, word in enumerate(words) if word.contains(x)]
