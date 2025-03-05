class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if ch not in word:
            return word
        
        stack = []
        for i in range(len(word)):
            stack.append(word[i])
            if word[i] == ch:
                break
        stack = stack[::-1]
        stack += list(word[i+1:])
        return ''.join(stack)
