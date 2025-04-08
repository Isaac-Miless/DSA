class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        # make sure word1 is bigger
        char = 0
        res = ""
        
        while char < len(word1) or char < len(word2):
            if char < len(word1): res += word1[char]
            if char < len(word2): res += word2[char]
            char += 1
        
        return res
